from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}),label='کلمه عبور')


class RegisterForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'نام کاربری'}),label='نام کاربری')
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ایمیل'}),label= 'ایمیل',validators=[validators.EmailValidator('ایمیل وارد شده معتبر نیست!')])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'کلمه عبور'}),label='کلمه عبور',validators=[validators.MinLengthValidator(6,'پسورد نمیتواند کمتر از 6 کاراکتر باشد!')])
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور'}),label='تکرار کلمه ی عبور')

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه های عبور باهم مغایرت دارند!')
        return password

    def clean_user_name(self):
        username = self.cleaned_data.get('user_name')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('این نام کاربری قبلا ثبت شده است')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('کاربری با این ایمیل قبلا ثبت نام کرده است')
        return email