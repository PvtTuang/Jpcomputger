# Generated by Django 4.2.9 on 2024-05-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0023_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ตรวจสอบคำสั่งซื้อ', 'ตรวจสอบคำสั่งซื้อ'), ('กำลังจัดส่ง', 'กำลังจัดส่ง'), ('จัดส่งสำเร็จ', 'จัดส่งสำเร็จ'), ('ขอคืนสินค้า', 'ขอคืนสินค้า'), ('คืนสินค้าสำเร็จ', 'คืนสินค้าสำเร็จ')], default='ตรวจสอบคำสั่งซื้อ', max_length=20),
        ),
    ]
