from django import forms
from .models import TransportOrder

class TransportOrderForm(forms.ModelForm):
    courier = forms.ChoiceField(choices=TransportOrder.COURIER, label='Courier')
    parcel_number = forms.CharField(label='Parcel number')


    class Meta:
        model = TransportOrder
        fields = ['courier', 'parcel_number',  'delivery_date']
        
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
        }
