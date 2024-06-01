from django.shortcuts import render, redirect ,get_object_or_404
from .forms import SalesHistoryForm
from posts.models import Product
from django.contrib import messages
from sell.models import SalesHistory
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Sum
import plotly.graph_objs as go
from plotly.offline import plot
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def user_is_owner(user):
    return user.is_authenticated and user.profile.role.name == 'Owner'

@login_required
@user_passes_test(user_is_owner, login_url='/')
def sales_history(request):
    all_sales = SalesHistory.objects.all()

    # Daily Sales
    daily_sales = SalesHistory.objects.filter(sold_at__date=timezone.now().date())
    daily_total_price = daily_sales.aggregate(total_price=Sum('product__price'))['total_price'] or 0

    # Monthly Sales
    this_month = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    next_month = (this_month + timedelta(days=32)).replace(day=1)
    monthly_sales = SalesHistory.objects.filter(sold_at__gte=this_month, sold_at__lt=next_month)
    monthly_total_price = monthly_sales.aggregate(total_price=Sum('product__price'))['total_price'] or 0

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    custom_sales = None
    total_price = None
    product_types = []
    quantities_sold = []
    graph_div = ""

    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
        custom_sales = SalesHistory.objects.filter(sold_at__range=[start_date, end_date])
        total_price = custom_sales.aggregate(total_price=Sum('product__price'))['total_price']

        for sale in custom_sales:
            product_types.append(str(sale.product.product_type)) 
            quantities_sold.append(sale.quantity_sold)

        trace = go.Bar(x=product_types, y=quantities_sold)

        layout = go.Layout(
            title='ประวัติการขายที่กำหนดเอง',
            xaxis=dict(title='ประเภทสินค้า'),
            yaxis=dict(title='จำนวนที่ขาย'),
            showlegend=False
        )

        fig = go.Figure(data=[trace], layout=layout)
        graph_div = plot(fig, output_type='div')

    return render(request, 'sell/sales_history.html', {'all_sales': all_sales, 'daily_sales': daily_sales,
                                                       'daily_total_price': daily_total_price, 'monthly_sales': monthly_sales,
                                                       'monthly_total_price': monthly_total_price, 'custom_sales': custom_sales,
                                                       'total_price': total_price, 'graph_div': graph_div})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def sell_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = SalesHistoryForm(request.POST)
        if form.is_valid():
            quantity_sold = form.cleaned_data['quantity_sold']
            
            if product.quantity >= quantity_sold:
                product.quantity -= quantity_sold
                product.save()
                sales_history = form.save(commit=False)
                sales_history.product = product
                sales_history.save()
                messages.success(request, 'Product sold successfully.')
                return redirect('sales_history')
            else:
                messages.error(request, "Not enough product quantity for sale.")
    else:
        form = SalesHistoryForm(initial={'product': product})

    return render(request, 'sell/sell_product.html', {'form': form, 'product': product})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def delete_sales_history(request, sale_id):
    sale = get_object_or_404(SalesHistory, id=sale_id)
    product = sale.product
    if request.method == 'POST':
        product.quantity += sale.quantity_sold
        product.save()
        sale.delete()
        messages.success(request, 'Sale history deleted successfully.')
    return redirect('sales_history')

search_mapping = {
    'คอมพิวเตอร์': 'computer',
    'โน๊ตบุ๊ค': 'notebook',
    'จอภาพ': 'monitor',
    'จอ': 'monitor',
    'เมาส์': 'mousekeyboard',
    'เมาส์และคีย์บอร์ด': 'mousekeyboard',
    'คีย์บอร์ด': 'mousekeyboard',
    'หูฟังและลำโพง': 'headphonespeaker',
    'หูฟัง': 'headphonespeaker',
    'ลำโพง': 'headphonespeaker',
    'เครื่องพิมพ์': 'printer',
    'เครื่องปริ้น': 'printer',
    'การ์ดหน่วยความจำ': 'sdcards_usb',
    'การ์ดหน่วยความจำและแฟลชไดร์ฟ': 'sdcards_usb',
    'แฟลชไดร์ฟ': 'sdcards_usb',
    'อุปกรณ์เชื่อมต่อ': 'connectivitydevice',
    'สายต่อ': 'connectivitydevice',
    'สายเคเบิ้ล': 'connectivitydevice'
}

@login_required
@user_passes_test(user_is_owner, login_url='/')
def search_sell_results(request):
    query = request.GET.get('q')
    products = None

    if query in search_mapping:
        query = search_mapping[query]
    
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |     
            Q(product_type__name__icontains=query) |     
            Q(computer__brand__icontains=query) |
            Q(notebook__brand__icontains=query) |     
            Q(monitor__brand__icontains=query) |     
            Q(mousekeyboard__brand__icontains=query) |     
            Q(headphonespeaker__brand__icontains=query) |     
            Q(printer__brand__icontains=query) |     
            Q(sdcards_usb__brand__icontains=query) |     
            Q(connectivitydevice__brand__icontains=query)    
        ).distinct() 
    
    return render(request, 'sell/sell_product.html', {'products': products,})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def computer_filter(request):
    products = Product.objects.filter(computer__isnull=False).distinct()
    return render(request, 'sell/sell_product.html', {'products': products})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def notebook_filter(request):
    products = Product.objects.filter(notebook__isnull=False).distinct()
    return render(request, 'sell/sell_product.html', {'products': products})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def monitor_filter(request):
    products = Product.objects.filter(monitor__isnull=False).distinct()
    return render(request, 'sell/sell_product.html', {'products': products})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def mousekeyboard_filter(request):
    products = Product.objects.filter(mousekeyboard__isnull=False).distinct()
    return render(request, 'sell/sell_product.html', {'products': products})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def headphonespeaker_filter(request):
    products = Product.objects.filter(headphonespeaker__isnull=False).distinct()
    return render(request, 'sell/sell_product.html', {'products': products})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def printer_filter(request):
    products = Product.objects.filter(printer__isnull=False).distinct()
    return render(request, 'sell/sell_product.html', {'products': products})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def sdcards_usb_filter(request):
    products = Product.objects.filter(sdcards_usb__isnull=False).distinct()
    return render(request, 'sell/sell_product.html', {'products': products})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def connectivitydevice_filter(request):
    products = Product.objects.filter(connectivitydevice__isnull=False).distinct()
    return render(request, 'sell/sell_product.html', {'products': products})