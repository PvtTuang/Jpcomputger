# Generated by Django 4.2.9 on 2024-05-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0008_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportorder',
            name='courier',
            field=models.CharField(choices=[('ไปรษณีย์ไทย', 'ไปรษณีย์ไทย'), ('Shopee express', 'Shopee express'), ('Kerry Express', 'Kerry Express'), ('BEST EXPRESS', 'BEST EXPRESS'), ('J&T EXPRESS', 'J&T EXPRESS'), ('FLASH EXPRESS', 'FLASH EXPRESS'), ('DHL EXPRESS', 'DHL EXPRESS')], max_length=20),
        ),
        migrations.AlterField(
            model_name='transportorder',
            name='delivery_status',
            field=models.CharField(choices=[('กำลังจัดส่ง', 'กำลังจัดส่ง'), ('จัดส่งเสร็จสิ้น', 'จัดส่งเสร็จสิ้น')], default='กำลังจัดส่ง', max_length=100),
        ),
    ]
