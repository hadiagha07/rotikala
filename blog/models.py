from django.db import models, IntegrityError, transaction
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(
        max_length=250,
        validators=[MinLengthValidator(5)],
        verbose_name="عنوان"
    )
    description = models.TextField(verbose_name="توضیحات")
    publish = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    views = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدید")
    reading_time = models.PositiveIntegerField(verbose_name="مدت زمان مطالعه")
    slug = models.SlugField(unique=True, max_length=250, blank=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['publish']),
        ]
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="پست"
    )
    name = models.CharField(
        max_length=80,
        validators=[MinLengthValidator(2)],
        verbose_name="نام"
    )
    body = models.TextField(verbose_name="متن نظر")
    time = models.DateTimeField(default=timezone.now, verbose_name="زمان ایجاد")
    active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        ordering = ['-time']
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return f'نظر توسط {self.name} در {self.post}'

class Image(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="پست"
    )
    image_file = models.ImageField(
        upload_to="uploads/%Y/",
        blank=True,
        null=True,
        verbose_name="فایل تصویر"
    )
    title = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="عنوان"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="توضیحات"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"

    def __str__(self):
        return self.title if self.title else "بدون عنوان"

    def delete(self, *args, **kwargs):
        self.image_file.delete(save=False)
        super().delete(*args, **kwargs)