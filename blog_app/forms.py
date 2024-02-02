from .models import BlogPost
from django import forms
from django.forms import ModelForm


class BlogForm(forms.ModelForm):

    class Meta:
        model= BlogPost
        fields='__all__'