# Generated by Django 4.2.9 on 2024-05-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_computer_mainboard_computer_powersupply_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='mainboard',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='powersupply',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='camera',
            field=models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='display',
            field=models.CharField(choices=[('13.3', '13.3'), ('14.0', '14.0'), ('15.6', '15.6'), ('16.0', '16.0'), ('17.3', '17.3')], max_length=50, null=True),
        ),
    ]
