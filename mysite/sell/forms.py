from django import forms
from .models import SalesHistory

class SalesHistoryForm(forms.ModelForm):
    class Meta:
        model = SalesHistory
        fields = ['quantity_sold']
