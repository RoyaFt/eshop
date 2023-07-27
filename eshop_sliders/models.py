from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان')
    descriptions = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name='تصویر')


    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title