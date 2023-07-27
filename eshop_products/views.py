import itertools

from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, ProductGallery
from django.http import Http404
from eshop_products_category.models import ProductCategory
from eshop_tag.models import Tag


# Create your views here.

class ProductsList(ListView):
    template_name = 'product_list.html'
    paginate_by = 6

    def get_context_data(self,**kwargs):
        categories = ProductCategory.objects.all()
        context = super(ProductsList,self).get_context_data(**kwargs)
        context['categories'] = categories
        return context

    def get_queryset(self):
        return Product.objects.get_active_products()

class ProductListByCategory(ListView):
    template_name = 'product_list.html'
    paginate_by = 6


    def get_queryset(self):
        print(self.kwargs)
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد!')
        return Product.objects.get_products_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def product_detail(request, my_product_id=None, *args, **kwargs):
    my_product_id = kwargs['productId']

    product = Product.objects.get_by_id(my_product_id)
    categories = ProductCategory.objects.all()
    gallery = ProductGallery.objects.filter(product_id = my_product_id)
    related_products = Product.objects.filter(categories__product = product).distinct()
    grouped_galleries = list(my_grouper(3, gallery))
    grouped_related_products = my_grouper(3,related_products)


    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')

    context = {
        'product': product,
        'categories' : categories,
        'galleries' : grouped_galleries,
        'related_products' : related_products
    }

    #    = Tag.objects.first()
    # print (tag.products.all())
    return render(request, 'product_detail.html', context)


class SearchProductsView(ListView):
    template_name = 'product_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_products()


