from django.urls import path
from .views import *

urlpatterns = [
    
    path('', list_all_orders, name='list_all_orders'),
    path('transport_order/<int:order_id>/', transport_order_detail, name='transport_order_detail'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
    path('confirm_received/<int:order_id>/', confirm_received, name='confirm_received'),
    path('check_page/', check_page , name='check_page'),
    path('return_order/<int:order_id>/', return_order, name='return_order'),
    path('confirm_return_order/<int:order_id>/', confirm_return_order, name='confirm_return_order'),
    path('cancel_order/<int:order_id>/', cancel_order, name='cancel_order'),
]
