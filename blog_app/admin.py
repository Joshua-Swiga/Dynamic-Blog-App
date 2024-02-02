from django.contrib import admin
from .models import BlogPost, RegisterModel, LoginModel
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(RegisterModel)
admin.site.register(LoginModel)