# Generated by Django 4.1.2 on 2025-01-15 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='اسم دسته\u200cبندی')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True, verbose_name='اسلاگ')),
                ('image', models.ImageField(upload_to='media/', verbose_name='عکس دسته\u200cبندی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی\u200cها',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='اسم محصول')),
                ('nickname', models.CharField(max_length=400, verbose_name='اسم محصول به انگلیسی')),
                ('product_code', models.CharField(blank=True, max_length=6, unique=True, verbose_name='کد محصول')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
