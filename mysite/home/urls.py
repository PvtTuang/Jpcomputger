from django.urls import path
from home.views import *

urlpatterns = [
    path('',home,name='home'),
    path('product_detail/<int:id>/',product_detail,name='product_detail'),
    path('computer/',computer_all,name='computer_all'),
    path('notebook/',notebook_all,name='notebook_all'),
    path('monitor/',monitor_all,name='monitor_all'),
    path('mousekeyboard/',mousekeyboard_all,name='mousekeyboard_all'),
    path('headphonespeaker/',headphonespeaker_all,name='headphonespeaker_all'),
    path('printer/',printer_all,name='printer_all'),
    path('sdcards_usb/',sdcards_usb_all,name='sdcards_usb_all'),
    path('connectivitydevice/',connectivitydevice_all,name='connectivitydevice_all'),
]
