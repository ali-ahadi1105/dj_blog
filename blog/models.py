from django.db import models
from django.utils import timezone
from extentions.utils import jalali_converter

# Create your models here.

class Article(models.Model):
    
    STATUS_CHOICES = (
        ('p', 'منتشرشده'),
        ('d', 'پیش‌نویش'),
    )
    
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.CharField(max_length=100, unique=True, verbose_name='آدرس مقاله')
    description = models.TextField(verbose_name='محتوا')
    thumbnail = models.ImageField(upload_to="images", verbose_name='تصویر مقاله')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
    
    def __str__(self):
        return self.title
    
    def jpublish(self):
        return jalali_converter(self.publish)
    
    jpublish.short_description = "زمان انتشار"