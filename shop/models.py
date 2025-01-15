from django.db import models
from django.utils.text import slugify
from django.utils import timezone



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

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name




