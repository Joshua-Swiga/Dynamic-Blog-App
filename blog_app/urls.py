from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'), #The home page where posts will be outlined
    path("users_post/", views.user_post, name='user_post'), #include form model for registered users to add their posts
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
    path("posts/<int:pk>/", views.post, name='post'), #uses dynamic routing to display different posts

#Remove extensions 
]