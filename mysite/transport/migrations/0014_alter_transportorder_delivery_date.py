# Generated by Django 4.2.9 on 2024-05-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0013_alter_transportorder_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportorder',
            name='delivery_date',
            field=models.DateField(null=True),
        ),
    ]
