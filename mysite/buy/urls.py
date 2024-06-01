from django.urls import path
from buy.views import *

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'), 
    path('cart/update/<int:cart_item_id>/', update_cart, name='update_cart'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('payment/<int:order_id>/', make_payment, name='make_payment'),
    path('upload_slip/<int:order_id>/', upload_slip, name='upload_slip'),
    path('show_orders/', show_orders, name='show_orders'),
    path('create_order/<int:cart_id>/', create_order, name='create_order'),
    path('add_shipping_address/', add_shipping_address, name='add_shipping_address'),
    path('view_shipping_addresses/', view_shipping_addresses, name='view_shipping_addresses'),
    path('edit_shipping_address/<int:address_id>/', edit_shipping_address, name='edit_shipping_address'),
    path('delete_shipping_address/<int:address_id>/', delete_shipping_address, name='delete_shipping_address'),
    path('get_shipping_address/<int:order_id>/', get_shipping_address, name='get_shipping_address'),
    path('like/<int:product_id>/', like_product, name='like_product'),
    path('liked-products/', liked_products, name='liked_products'),
    path('unlike/<int:like_id>/', unlike_product, name='unlike_product'),
]