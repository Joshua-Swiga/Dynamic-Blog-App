from .models import BlogPost, RegisterModel, LoginModel
from django import forms
from django.forms import ModelForm


class BlogForm(forms.ModelForm):

    class Meta:
        model= BlogPost
        fields='__all__'


class RegisterForm(forms.ModelForm):
    
    password_1=forms.CharField(widget=forms.PasswordInput)
    password_2=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=RegisterModel
        fields='__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model= LoginModel
        fields='__all__'
