from django.contrib import admin
from buy.models import *

# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(ShippingAddress)
admin.site.register(Like)