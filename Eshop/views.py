from django.shortcuts import render



def header(request, *args, **kwargs):
    context = {
        'test':'تست2'
    }
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    context = {
        'aboat_us':'این یک فوتر تستی توسط رویا میباشد'
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    context = {
        'data': 'new date',
    }
    return render(request, 'home_page.html', context)

