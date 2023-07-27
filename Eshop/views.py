from django.shortcuts import render

from eshop_settings.models import SiteSetting
from eshop_sliders.models import Slider


def header(request, *args, **kwargs):
    context = {
        'test':'تست2'
    }
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting':site_setting
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    sliders = Slider.objects.all()
    context = {
        'sliders' : sliders,
        'data': 'new date',
    }
    return render(request, 'home_page.html', context)

