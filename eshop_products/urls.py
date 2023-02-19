from django.urls import path

from .views import ProductsList, product_detail, SearchProductsView

urlpatterns = [
    path('products/', ProductsList.as_view()),
    path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
]
