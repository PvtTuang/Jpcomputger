from django.shortcuts import render , redirect , get_object_or_404
from posts.models import *


# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home/home.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product , pk=id)
    return render(request , 'home/detail_product.html',{'product' : product})

def computer_all(request):
    products = Product.objects.all()
    return render(request , 'home/product/computer.html',{'products' : products})

def notebook_all(request):
    products = Product.objects.all()
    return render(request , 'home/product/notebook.html',{'products' : products})

def monitor_all(request):
    products = Product.objects.all()
    return render(request , 'home/product/monitor.html',{'products' : products})

def mousekeyboard_all(request):
    products = Product.objects.all()
    return render(request , 'home/product/mousekeyboard.html',{'products' : products})

def headphonespeaker_all(request):
    products = Product.objects.all()
    return render(request , 'home/product/headphonespeaker.html',{'products' : products})

def printer_all(request):
    products = Product.objects.all()
    return render(request , 'home/product/printer.html',{'products' : products})

def sdcards_usb_all(request):
    products = Product.objects.all()
    return render(request , 'home/product/sdcards_usb.html',{'products' : products})

def connectivitydevice_all(request):
    products = Product.objects.all()
    return render(request , 'home/product/connectivitydevice.html',{'products' : products})