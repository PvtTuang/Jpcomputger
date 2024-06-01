from django.shortcuts import render, get_object_or_404, redirect
from .models import TransportOrder
from .forms import TransportOrderForm
from buy.models import Order
from django.db import transaction
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from accounts.decorators import block_role_required
# Create your views here.

def user_is_owner(user):
    return user.is_authenticated and user.profile.role.name == 'Owner'

@login_required
@user_passes_test(user_is_owner, login_url='/')
def list_all_orders(request):
    orders = Order.objects.all()
    orders_with_totals = []
    for order in orders:
        total_amount = sum(item.product.price * item.quantity for item in order.cart.cartitem_set.all())
        orders_with_totals.append((order, total_amount))

    return render(request, 'transport/list_all_orders.html', {'orders_with_totals': orders_with_totals})

@login_required
@transaction.atomic
@block_role_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    shipping_addresses = order.shipping_addresses.all()
    total_amount = sum(item.product.price * item.quantity for item in order.cart.cartitem_set.all())

    if request.method == 'POST':
        form = TransportOrderForm(request.POST)
        if form.is_valid():
            transport_order = form.save(commit=False)
            transport_order.order = order
            transport_order.delivery_status = 'จัดส่งเสร็จสิ้น'
            transport_order.save()

            order.status = 'กำลังจัดส่ง'
            order.save()

            return redirect('order_detail', order_id=order.id)
    else:
        form = TransportOrderForm()

    return render(request, 'transport/order_detail.html', {'order': order, 'total_amount': total_amount, 'form': form, 'shipping_addresses': shipping_addresses})

@login_required
@block_role_required
def transport_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.status == 'ตรวจสอบคำสั่งซื้อ':
        return redirect('check_page')
    transport_order = get_object_or_404(TransportOrder, order_id=order_id)
    now = datetime.now().date()  
    seven_days_from_delivery = transport_order.delivery_date + timedelta(days=7)
    can_return = transport_order.delivery_status == 'จัดส่งเสร็จสิ้น' and now < seven_days_from_delivery

    return render(request, 'transport/transport_order_detail.html', {'transport_order': transport_order, 'can_return': can_return})

@login_required
@block_role_required
def confirm_return_order(request, order_id):
    transport_order = get_object_or_404(TransportOrder, order__id=order_id)
    
    if request.method == 'POST':
        transport_order.delivery_status = 'คืนสินค้า'
        transport_order.save()

        order = transport_order.order
        order.status = 'คืนสินค้า'
        order.save()
        
        return redirect('list_all_orders')

    return render(request, 'transport/return_order.html', {'transport_order': transport_order})

@login_required
@block_role_required
def check_page(request):
    return render(request,'transport/check_page.html')

@login_required
@block_role_required
def confirm_received(request, order_id):
    transport_order = get_object_or_404(TransportOrder, order_id=order_id)
    if request.method == 'POST':
        transport_order.delivery_status = 'จัดส่งเสร็จสิ้น'
        transport_order.save()

        order = transport_order.order
        order.status = 'จัดส่งสำเร็จ'
        order.save()
        
        return redirect('show_orders')
    return redirect('transport_order_detail', order_id=order.id)

@login_required
@block_role_required
def return_order(request, order_id):
    transport_order = get_object_or_404(TransportOrder, order__id=order_id)
    
    if request.method == 'POST':
        transport_order.delivery_status = 'ขอคืนสินค้า'
        transport_order.save()

        order = transport_order.order
        order.status = 'ขอคืนสินค้า'
        order.save()
        
        return redirect('transport_order_detail', order_id=order_id)

    return render(request, 'transport/return_order.html', {'transport_order': transport_order})


@login_required
@user_passes_test(user_is_owner, login_url='/')
def cancel_order(request, order_id):
    transport_order = get_object_or_404(TransportOrder, order__id=order_id)
    if request.method == 'POST':
        transport_order.delivery_status = 'ยกเลิกคำสั่งซื้อ'
        transport_order.save()

        order = transport_order.order
        order.status = 'ยกเลิกคำสั่งซื้อ'
        order.save()

        return redirect('order_detail', order_id=order_id)

    return render(request, 'transport/cancel_order.html', {'transport_order': transport_order})