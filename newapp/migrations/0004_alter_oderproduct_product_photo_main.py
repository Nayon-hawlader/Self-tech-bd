# Generated by Django 3.2.3 on 2021-07-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_alter_oderproduct_product_photo_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oderproduct',
            name='product_photo_main',
            field=models.ImageField(default='trends_photo/best_5.png', upload_to='order_product_image', verbose_name='order_product_image'),
        ),
    ]
