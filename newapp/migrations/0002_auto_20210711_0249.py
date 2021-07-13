# Generated by Django 3.2.3 on 2021-07-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_background',
            field=models.ImageField(upload_to='banner_background/', verbose_name='banner_background'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='product_photo',
            field=models.ImageField(blank=True, default='../placeholder.png', upload_to='banner_product_photo/', verbose_name='banner_product_photo'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='blog_image/top_baner4.jpg', upload_to='blog_image/', verbose_name='blog_image'),
        ),
        migrations.AlterField(
            model_name='deals_of_the_week',
            name='product_photo',
            field=models.ImageField(blank=True, default='../placeholder.png', upload_to='Deals_of_the_Week_photo/', verbose_name='Deals_of_the_Week_photo'),
        ),
        migrations.AlterField(
            model_name='featured_product',
            name='product_photo_main',
            field=models.ImageField(blank=True, default='../placeholder.png', upload_to='Featured_product_photo/', verbose_name='product_photo_main'),
        ),
        migrations.AlterField(
            model_name='featured_product',
            name='product_slider_photo_color_merun',
            field=models.ImageField(blank=True, default='../placeholder.png', upload_to='c/', verbose_name='product_slider_photo_color_merun'),
        ),
        migrations.AlterField(
            model_name='oderproduct',
            name='product_photo_main',
            field=models.ImageField(default='trends_photo/best_5.png', upload_to='order_product_image', verbose_name='order_product_image'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_photo_main',
            field=models.ImageField(default='trends_photo/best_5.png', upload_to='order_image', verbose_name='order_image'),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='product_photo_main',
            field=models.ImageField(default='trends_photo/best_5.png', upload_to='shopcart_image', verbose_name='shopcart_image'),
        ),
    ]