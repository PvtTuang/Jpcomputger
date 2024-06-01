# Generated by Django 4.2.9 on 2024-05-15 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0023_alter_product_image1_alter_product_image2_and_more'),
        ('buy', '0021_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='product',
        ),
        migrations.AddField(
            model_name='like',
            name='products',
            field=models.ManyToManyField(to='posts.product'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
