from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class CategoryMenu(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم')

    class Meta:
        verbose_name = 'منوی هدر'
        verbose_name_plural = 'منوی هدر'

    def __str__(self):
        return self.name

class ItemCategoryMenu(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم')



class SubCategory(models.Model):
    category = models.ForeignKey(ItemCategoryMenu, related_name='subcategories', on_delete=models.CASCADE, verbose_name='موضوع')
    name = models.CharField(max_length=100)
    url = models.URLField(verbose_name='لینک')

    class Meta:
        verbose_name = 'موضوع های منو'
        verbose_name_plural = 'موضوع های منو'

    def __str__(self):
        return self.name


class Sliders(models.Model):
    main_slider = models.ImageField(upload_to="uploads/%Y/%m/", blank=True, null=True, verbose_name='فایل تصویر')
    slider1 = models.ImageField(upload_to="uploads/%Y/%m/", blank=True, null=True, verbose_name='فایل تصویر')
    slider2 = models.ImageField(upload_to="uploads/%Y/%m/", blank=True, null=True, verbose_name='فایل تصویر')
    slider3 = models.ImageField(upload_to="uploads/%Y/%m/", blank=True, null=True, verbose_name='فایل تصویر')
    slider4 = models.ImageField(upload_to="uploads/%Y/%m/", blank=True, null=True, verbose_name='فایل تصویر')
    slider5 = models.ImageField(upload_to="uploads/%Y/%m/", blank=True, null=True, verbose_name='فایل تصویر')


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="اسم دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="اسلاگ")
    image = models.ImageField(upload_to='media/', verbose_name="عکس دسته‌بندی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:  # اگر اسلاگ وجود نداشت، از نام ایجاد کن
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    name = models.CharField(max_length=400, verbose_name='اسم محصول')
    nickname = models.CharField(max_length=400, verbose_name='اسم محصول به انگلیسی')
    product_code = models.CharField(max_length=6, unique=True, blank=True, verbose_name="کد محصول")
    colors = models.ManyToManyField(Color)
    price_before_dis = models.PositiveBigIntegerField(default=0, blank=True, null=True, verbose_name='قیمت')
    price = models.PositiveBigIntegerField(default=0, blank=True, null=True, verbose_name='قیمت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name


class Feature(models.Model):
    product = models.ForeignKey(Product, verbose_name='محصول', related_name='features', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='اسم ویزگی')
    value = models.CharField(max_length=100, verbose_name='ولیو ویزگی')

    def __str__(self):
        return f"{self.name}: {self.value}"


class Image(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='محصول')
    image_file = models.ImageField(upload_to="uploads/%Y/%m/", blank=True, null=True, verbose_name='فایل تصویر')
    created = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')


class Size(models.Model):
    size = models.IntegerField(verbose_name='سایز کفش')

