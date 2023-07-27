from django.contrib import admin

# Register your models here.

from .models import Product, ProductGallery
from eshop_products_category.models import ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
