from django.db.models import Q
from django.db import models
import os

from eshop_products_category.models import ProductCategory


# Create your models here.

class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()

    def get_products_by_category(self,category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name,active=True)


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    categories = models.ManyToManyField(ProductCategory,blank=True,verbose_name='دسته بندی ها')

    objects = ProductsManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"

class ProductGallery(models.Model):
    title = models.CharField(max_length=150 ,verbose_name='عنوان')
    image = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name='تصویر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='تصویر برای محصول')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

    def __str__(self):
        return self.title
