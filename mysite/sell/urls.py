from django.urls import path
from sell.views import *

urlpatterns = [
    path('', sales_history, name='sales_history'),
    path('sell_product/<int:product_id>/', sell_product, name='sell_product'),
    path('search_sell_results/', search_sell_results, name='search_sell_results'),
    path('delete-sales-history/<int:sale_id>/', delete_sales_history, name='delete_sales_history'),
    path('computer/', computer_filter, name='computer_filter'),
    path('notebook/', notebook_filter, name='notebook_filter'),
    path('monitor/', monitor_filter, name='monitor_filter'),
    path('mousekeyboard/', mousekeyboard_filter, name='mousekeyboard_filter'),
    path('headphonespeaker/', headphonespeaker_filter, name='headphonespeaker_filter'),
    path('printer/', printer_filter, name='printer_filter'),
    path('sdcards_usb/', sdcards_usb_filter, name='sdcards_usb_filter'),
    path('connectivitydevice/', connectivitydevice_filter, name='connectivitydevice_filter'),
]