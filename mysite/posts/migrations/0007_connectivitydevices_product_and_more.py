# Generated by Django 4.2.9 on 2024-04-20 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_producttype_alter_computer_warranty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectivitydevices',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.product'),
        ),
        migrations.AddField(
            model_name='headphonespeakers',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.product'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.product'),
        ),
        migrations.AddField(
            model_name='mousekeyboard',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.product'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.product'),
        ),
        migrations.AddField(
            model_name='printers',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.product'),
        ),
        migrations.AddField(
            model_name='sdcards_usbs',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.product'),
        ),
    ]
