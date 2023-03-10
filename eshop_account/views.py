from django.contrib.auth import authenticate, login, get_user_model, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from eshop_account.forms import LoginForm, RegisterForm


# Create your views here.
def login_page(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request,username=user_name,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد!')
    context={
        'login_form':login_form
    }
    return render(request,'login.html',context)


def register(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=user_name,email=email,password=password)
        return redirect('login')

    context={
        'register_form':register_form
    }
    return render (request,'register.html',context)