# Generated by Django 4.1.2 on 2025-01-17 07:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم')),
            ],
            options={
                'verbose_name': 'منوی هدر',
                'verbose_name_plural': 'منوی هدر',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hex_code', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(verbose_name='سایز کفش')),
            ],
        ),
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_slider', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/', verbose_name='فایل تصویر')),
                ('slider1', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/', verbose_name='فایل تصویر')),
                ('slider2', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/', verbose_name='فایل تصویر')),
                ('slider3', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/', verbose_name='فایل تصویر')),
                ('slider4', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/', verbose_name='فایل تصویر')),
                ('slider5', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/', verbose_name='فایل تصویر')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاریخ ایجاد'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='قیمت'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_before_dis',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='قیمت'),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(verbose_name='لینک')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='shop.itemcategorymenu', verbose_name='موضوع')),
            ],
            options={
                'verbose_name': 'موضوع های منو',
                'verbose_name_plural': 'موضوع های منو',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/', verbose_name='فایل تصویر')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product', verbose_name='محصول')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم ویزگی')),
                ('value', models.CharField(max_length=100, verbose_name='ولیو ویزگی')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='shop.product', verbose_name='محصول')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='shop.color'),
        ),
    ]
