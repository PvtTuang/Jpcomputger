# Generated by Django 4.2.9 on 2024-05-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0009_alter_transportorder_courier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportorder',
            name='delivery_status',
            field=models.CharField(choices=[('กำลังจัดส่ง', 'กำลังจัดส่ง'), ('จัดส่งเสร็จสิ้น', 'จัดส่งเสร็จสิ้น'), ('คืนสินค้า', 'คืนสินค้า'), ('คืนสินค้าสำเร็จ', 'คืนสินค้าสำเร็จ')], default='กำลังจัดส่ง', max_length=100),
        ),
    ]
