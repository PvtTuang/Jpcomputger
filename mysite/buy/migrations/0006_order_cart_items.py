# Generated by Django 4.2.9 on 2024-05-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0005_remove_order_user_order_cart_alter_order_slip_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart_items',
            field=models.ManyToManyField(to='buy.cartitem'),
        ),
    ]
