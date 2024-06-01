from django.db import models
from posts.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    STATUS_ALL = [
        ('อยู่ในตะกร้า', 'อยู่ในตะกร้า'),
        ('ชำระเงินแล้ว', 'ชำระเงินแล้ว'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_ALL, default='อยู่ในตะกร้า')

    def update_status(self, new_status):
        self.status = new_status
        self.save()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
class Order(models.Model):
    STATUS_ALL = [
        ('ตรวจสอบคำสั่งซื้อ','ตรวจสอบคำสั่งซื้อ'),
        ('กำลังจัดส่ง','กำลังจัดส่ง'),
        ('จัดส่งสำเร็จ','จัดส่งสำเร็จ'),
        ('ขอคืนสินค้า','ขอคืนสินค้า'),
        ('คืนสินค้าสำเร็จ','คืนสินค้าสำเร็จ'),
    ]
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True) 
    status = models.CharField(max_length=20, choices=STATUS_ALL, default='ตรวจสอบคำสั่งซื้อ')
    slip_image = models.ImageField(upload_to='static/slips/', null=True, blank=True)
    cart_items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class ShippingAddress(models.Model):
    orders = models.ManyToManyField(Order, related_name='shipping_addresses')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100,null=True,blank=False)
    lastname = models.CharField(max_length=100,null=True,blank=False)
    number = models.CharField(max_length=10,blank=False)
    house_number = models.CharField(max_length=10,blank=False)
    swine = models.CharField(max_length=100,blank=False)
    subswine = models.CharField(max_length=100, blank=True, default='-')
    subdistrict = models.CharField(max_length=100,blank=False)
    district = models.CharField(max_length=100,blank=False)
    province = models.CharField(max_length=100,blank=False)
    postal_code = models.CharField(max_length=10,blank=False)

    def __str__(self):
        return f"{self.number}, {self.house_number}, {self.swine}, {self.subswine}, {self.subdistrict}, {self.district}, {self.province}, {self.postal_code}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)