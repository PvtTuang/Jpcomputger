from django.urls import path
from posts.views import *

urlpatterns = [
    path('', add_product, name='add_product'),
    path('products/', product_list, name='product_list'),
    path('update/<int:pk>/', product_update, name='product_update'),
    path('delete-product/<int:pk>/', delete_product, name='delete_product'),

    path('add-computer/<int:pk>/', add_item, {'form_class': ComputerForm, 'model_class': Computer}, name='add_computer'),
    path('add-notebook/<int:pk>/', add_item, {'form_class': NotebookForm, 'model_class': Notebook}, name='add_notebook'),
    path('add-monitor/<int:pk>/', add_item, {'form_class': MonitorForm, 'model_class': Monitor}, name='add_monitor'),
    path('add-mouse-keyboard/<int:pk>/', add_item, {'form_class': MouseKeyboardForm, 'model_class': MouseKeyboard}, name='add_mouse_keyboard'),
    path('add-headphone-speakers/<int:pk>/', add_item, {'form_class': HeadphoneSpeakersForm, 'model_class': HeadphoneSpeakers}, name='add_headphone_speakers'),
    path('add-printers/<int:pk>/', add_item, {'form_class': PrintersForm, 'model_class': Printers}, name='add_printers'),
    path('add-sd-cards-usbs/<int:pk>/', add_item, {'form_class': SDCards_USBsForm, 'model_class': SDCards_USBs}, name='add_sd_cards_usbs'),
    path('add-connectivity-devices/<int:pk>/', add_item, {'form_class': ConnectivityDevicesForm, 'model_class': ConnectivityDevices}, name='add_connectivity_devices'),

    path('update-computer/<int:pk>/', update_item, {'form_class': ComputerForm, 'model_class': Computer}, name='update_computer'),
    path('update-notebook/<int:pk>/', update_item, {'form_class': NotebookForm, 'model_class': Notebook}, name='update_notebook'),
    path('update-monitor/<int:pk>/', update_item, {'form_class': MonitorForm, 'model_class': Monitor}, name='update_monitor'),
    path('update-mouse-keyboard/<int:pk>/', update_item, {'form_class': MouseKeyboardForm, 'model_class': MouseKeyboard}, name='update_mouse_keyboard'),
    path('update-headphone-speakers/<int:pk>/', update_item, {'form_class': HeadphoneSpeakersForm, 'model_class': HeadphoneSpeakers}, name='update_headphone_speakers'),
    path('update-printers/<int:pk>/', update_item, {'form_class': PrintersForm, 'model_class': Printers}, name='update_printers'),
    path('update-sd-cards-usbs/<int:pk>/', update_item, {'form_class': SDCards_USBsForm, 'model_class': SDCards_USBs}, name='update_sd_cards_usbs'),
    path('update-connectivity-devices/<int:pk>/', update_item, {'form_class': ConnectivityDevicesForm, 'model_class': ConnectivityDevices}, name='update_connectivity_devices'),
    
    path('search/',search_results, name='search_results'),

]
