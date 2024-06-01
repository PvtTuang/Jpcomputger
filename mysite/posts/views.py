from django.shortcuts import render,redirect,get_object_or_404
from posts.forms import *
from posts.models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def user_is_owner(user):
    return user.is_authenticated and user.profile.role.name == 'Owner'

@login_required
@user_passes_test(user_is_owner, login_url='/')
def product_list(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'posts/product_list.html', {'products': products})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form = ProductForm()
    return render(request, 'posts/add_product.html', {'form': form})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def add_item(request, pk, form_class, model_class):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            if not model_class.objects.filter(product_id=pk).exists():
                item = form.save(commit=False)
                item.product = product
                item.save()
                product.has_detail = True  
                product.save()
            return redirect('product_list')
    else:
        form = form_class()
    return render(request, f'posts/add/add_{model_class.__name__.lower()}.html', {'form': form, 'product': product})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def update_item(request, pk, form_class, model_class):
    product = get_object_or_404(Product, pk=pk)
    item = get_object_or_404(model_class, product=product)
    
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('product_list') 
    else:
        form = form_class(instance=item) 
    return render(request, f'posts/update/update_{model_class.__name__.lower()}.html', {'form': form, 'item': item ,'product': product})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'posts/product_form.html', {'form': form})

@login_required
@user_passes_test(user_is_owner, login_url='/')
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    image_paths = [
        os.path.join(settings.MEDIA_ROOT, str(product.image1)),
        os.path.join(settings.MEDIA_ROOT, str(product.image2)),
        os.path.join(settings.MEDIA_ROOT, str(product.image3)),
    ]
    if request.method == 'POST':
        product.delete()
        for path in image_paths:
            if FileSystemStorage().exists(path):
                FileSystemStorage().delete(path)
        return redirect('product_list')

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

def search_results(request):
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
    else:
        products = Product.objects.all()
    
    return render(request, 'home/home.html', {'products': products})







