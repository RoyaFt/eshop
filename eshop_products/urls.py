from django.urls import path

from .views import ProductsList, product_detail, SearchProductsView, ProductListByCategory

urlpatterns = [
    path('products/', ProductsList.as_view(),name='products'),
    path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
    path('products/<category_name>',ProductListByCategory.as_view()),
]
