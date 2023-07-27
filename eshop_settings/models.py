from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان سایت')
    address = models.CharField(max_length=400,verbose_name='آدرس')
    phone = models.CharField(max_length=50,verbose_name= 'شماره ثابت')
    mobile = models.CharField(max_length=50,verbose_name='شماره موبایل')
    email = models.CharField(max_length=50,verbose_name='ایمیل')
    fax = models.CharField(max_length=50,verbose_name='فکس')
    about_us = models.TextField(verbose_name='درباره ی ما',blank=True,null=True)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات'

    def __str__ (self):
        return self.title
