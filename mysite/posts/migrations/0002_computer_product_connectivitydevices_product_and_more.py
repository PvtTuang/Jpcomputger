# Generated by Django 4.2.9 on 2024-04-16 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='product',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.product'),
        ),
        migrations.AddField(
            model_name='connectivitydevices',
            name='product',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.product'),
        ),
        migrations.AddField(
            model_name='headphonespeakers',
            name='product',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.product'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='product',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.product'),
        ),
        migrations.AddField(
            model_name='mousekeyboard',
            name='product',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.product'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='product',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.product'),
        ),
        migrations.AddField(
            model_name='printers',
            name='product',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.product'),
        ),
        migrations.AddField(
            model_name='sdcards_usbs',
            name='product',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.product'),
        ),
    ]
