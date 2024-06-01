from django import forms
from posts.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'

class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = '__all__'

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'

class MouseKeyboardForm(forms.ModelForm):
    class Meta:
        model = MouseKeyboard
        fields = '__all__'

class HeadphoneSpeakersForm(forms.ModelForm):
    class Meta:
        model = HeadphoneSpeakers
        fields = '__all__'

class PrintersForm(forms.ModelForm):
    class Meta:
        model = Printers
        fields = '__all__'

class SDCards_USBsForm(forms.ModelForm):
    class Meta:
        model = SDCards_USBs
        fields = '__all__'

class ConnectivityDevicesForm(forms.ModelForm):
    class Meta:
        model = ConnectivityDevices
        fields = '__all__'


