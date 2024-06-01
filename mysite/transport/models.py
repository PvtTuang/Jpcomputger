from django.db import models
from django.contrib.auth.models import User
from buy.models import Order

# Create your models here.

class TransportOrder(models.Model):
    COURIER = [
        ('ไปรษณีย์ไทย','ไปรษณีย์ไทย'),
        ('Shopee express','Shopee express'),
        ('Kerry Express','Kerry Express'),
        ('BEST EXPRESS','BEST EXPRESS'),
        ('J&T EXPRESS','J&T EXPRESS'),
        ('FLASH EXPRESS','FLASH EXPRESS'),
        ('DHL EXPRESS','DHL EXPRESS'),
    ]
    STATUS = [
        ('กำลังจัดส่ง','กำลังจัดส่ง'),
        ('จัดส่งเสร็จสิ้น','จัดส่งเสร็จสิ้น'),
        ('ขอคืนสินค้า','ขอคืนสินค้า'),
        ('คืนสินค้าสำเร็จ','คืนสินค้าสำเร็จ'),
        ('ยกเลิกคำสั่งซื้อ', 'ยกเลิกคำสั่งซื้อ'),
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    courier = models.CharField(choices=COURIER, max_length=20)
    parcel_number = models.CharField(max_length=10,blank=False)
    delivery_status = models.CharField(choices=STATUS, max_length=100, default='กำลังจัดส่ง') 
    delivery_date = models.DateField(null=True,blank=False)
