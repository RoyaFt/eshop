from django.urls import path
from . import views

urlpatterns = [
    path('/contact_us',views.contact_page,name='contact_us'),
]