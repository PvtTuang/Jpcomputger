from django.shortcuts import render, redirect, get_object_or_404
from buy.models import Cart, CartItem, Order, Product , ShippingAddress , Like
from buy.forms import CartItemForm, SlipForm , ShippingAddressForm
from promptpay import qrcode
import base64
from io import BytesIO
from django.db import transaction
from django.contrib.auth.decorators import login_required
from accounts.decorators import block_role_required
import requests

# Create your views here.

@login_required
@block_role_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    try:
        cart = Cart.objects.get(user=request.user, status='อยู่ในตะกร้า')
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user, status='อยู่ในตะกร้า')
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
    return redirect('view_cart')

@login_required
@block_role_required
def view_cart(request):
    carts = Cart.objects.filter(user=request.user, status='อยู่ในตะกร้า')
    if carts.exists():
        cart = carts.first()
        cart_items = cart.cartitem_set.all()
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        return render(request, 'buy/cart.html', {'cart_items': cart_items, 'total_price': total_price, 'cart': cart})
    else:
        return render(request, 'buy/cart.html', {'cart_items': [], 'total_price': 0})

@login_required
@block_role_required
def update_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    new_quantity = int(request.POST.get('quantity'))
    cart_item.quantity = new_quantity
    cart_item.save()
    return redirect('view_cart')

@login_required
@block_role_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required
@block_role_required
@transaction.atomic
def make_payment(request, order_id):
    order = Order.objects.get(pk=order_id)
    total_amount = sum(item.product.price * item.quantity for item in order.cart.cartitem_set.all())

    id_or_phone_number = "0626214110"
    payload_with_amount = qrcode.generate_payload(id_or_phone_number, total_amount)

    img = qrcode.to_image(payload_with_amount)

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    shipping_addresses = ShippingAddress.objects.filter(user=request.user)

    return render(request, 'buy/payment.html', {'payload': payload_with_amount, 
                                                'qr_code_image': img_str, 'order': order, 
                                                'total_amount': total_amount,
                                                'shipping_addresses': shipping_addresses, })

@login_required
@block_role_required
def create_order(request, cart_id):
    cart = get_object_or_404(Cart, pk=cart_id)
    existing_order = Order.objects.filter(cart=cart).first() 

    if existing_order:  
        return redirect('make_payment', order_id=existing_order.id)  

    if request.method == 'POST':
        form = SlipForm(request.POST, request.FILES)
        if form.is_valid():
            order = Order.objects.create(cart=cart, status='ตรวจสอบคำสั่งซื้อ', slip_image=form.cleaned_data['slip_image'])
            order.save()
            return redirect('make_payment', order_id=order.id)
    else:
        form = SlipForm()
    return render(request, 'buy/cart.html', {'form': form})

@login_required
@block_role_required
def get_shipping_address(request, order_id):
    order = Order.objects.get(pk=order_id)
    shipping_address = ShippingAddress.objects.filter(user=request.user)
    if request.method == 'POST':
        shipping_address_id= request.POST.get('shipping_address')
        shipping_address = get_object_or_404(ShippingAddress , pk = shipping_address_id)
        order.shipping_addresses.add(shipping_address)
        order.save()
        return redirect('make_payment', order_id=order_id)
    return render(request, 'buy/select_shipping_address.html', {' shipping_address': shipping_address})

@login_required
@block_role_required
@transaction.atomic
def upload_slip(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if request.method == 'POST':
        form = SlipForm(request.POST, request.FILES)
        
        if form.is_valid():
            order.slip_image = form.cleaned_data['slip_image']
            order.status = 'ตรวจสอบคำสั่งซื้อ'
            order.save()
        
            order.cart.status = 'ชำระเงินแล้ว'
            order.cart.save()

            user = request.user
            cart_items = order.cart.cartitem_set.all()
            for cart_item in cart_items:
                product = cart_item.product
                message = f'ผู้ใช้ {user.first_name} {user.last_name} เลขที่คำสั่งซื้อ {order.id} สนใจสินค้า {product.name} ราคา {product.price} บาท'
                
                line_notify_token = '2cub3WRYiIYwyA9F5BVAfA39THo5akVez9i5p7ScOKX'
                line_notify_api = 'https://notify-api.line.me/api/notify'
                headers = {'Authorization': f'Bearer {line_notify_token}'}
                payload = {'message': message}
                response = requests.post(line_notify_api, headers=headers, data=payload)

            if order.cart.status == 'ชำระเงินแล้ว':
                existing_order = Order.objects.filter(cart=order.cart).exists()
                
                if not existing_order:
                    new_order = Order.objects.create(cart=order.cart, status='ตรวจสอบคำสั่งซื้อ')
                    new_order.save()

            return redirect('order_detail', order_id=order_id)
    else:
        form = SlipForm()

    return render(request, 'buy/upload_slip.html', {'form': form})

@login_required
@block_role_required
def show_orders(request):
    user_orders = Order.objects.filter(cart__user=request.user)
    return render(request, 'buy/show_orders.html', {'user_orders': user_orders})

@login_required
@block_role_required
def add_shipping_address(request):
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.user = request.user
            shipping_address.save()
            return redirect('view_shipping_addresses')
    else:
        form = ShippingAddressForm()
    return render(request, 'buy/add_shipping_address.html', {'form': form})

@login_required
@block_role_required
def view_shipping_addresses(request):
    shipping_addresses = ShippingAddress.objects.filter(user=request.user)
    return render(request, 'buy/view_shipping_addresses.html', {'shipping_addresses': shipping_addresses})

@login_required
@block_role_required
def edit_shipping_address(request, address_id):
    address = get_object_or_404(ShippingAddress, pk=address_id)
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('view_shipping_addresses')
    else:
        form = ShippingAddressForm(instance=address)
    return render(request, 'buy/edit_shipping_addresses.html', {'form': form})

@login_required
@block_role_required
def delete_shipping_address(request, address_id):
    address = get_object_or_404(ShippingAddress, pk=address_id)
    if request.method == 'POST':
        address.delete()
        return redirect('view_shipping_addresses')
    return render(request, 'buy/view_shipping_addresses.html', {'address': address})

@login_required
@block_role_required
def like_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    
    if request.method == 'POST':
        if not Like.objects.filter(user=user, product=product).exists():
            like = Like.objects.create(user=user, product=product)
        return redirect('liked_products')
    else:
        return redirect('liked_products')

@login_required
@block_role_required
def unlike_product(request, like_id):
    like = get_object_or_404(Like, id=like_id)
    
    if request.method == 'POST' and request.user == like.user:
        like.delete()

    return redirect('liked_products')

@login_required
@block_role_required
def liked_products(request):
    liked_products = Like.objects.filter(user=request.user)
    return render(request, 'buy/liked_products.html', {'liked_products': liked_products})
