from django import forms
from buy.models import CartItem, Order , ShippingAddress

class CartItemForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, label='Quantity')

    class Meta:
        model = CartItem
        fields = ['quantity']

class SlipForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = ['slip_image']

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['firstname','lastname','number', 'house_number', 'swine', 'subswine', 'subdistrict', 'district', 'province', 'postal_code']



