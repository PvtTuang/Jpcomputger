# Generated by Django 4.2.9 on 2024-05-08 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0005_order_slip_image_alter_slip_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
        migrations.DeleteModel(
            name='Slip',
        ),
    ]