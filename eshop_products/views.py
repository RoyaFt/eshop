from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.http import Http404
from eshop_tag.models import Tag


# Create your views here.

class ProductsList(ListView):
    template_name = 'product_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()

class ProductListByCategory(ListView):
    template_name = 'product_list.html'
    paginate_by = 6


    def get_queryset(self):
        print(self.kwargs)
        return Product.objects.get_active_products()

def product_detail(request, *args, **kwargs):
    product_id = kwargs['productId']

    product = Product.objects.get_by_id(product_id)

    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')

    context = {
        'product': product
    }

    # tag = Tag.objects.first()
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


