from django.db import models

# Create your models here.
class BlogPost(models.Model):
    date=models.DateField(auto_now = True)
    title=models.CharField(max_length=100)
    body=models.TextField()

    def __str__(self) -> str:
        return "{self.title}"


class RegisterModel(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password_1=models.CharField(max_length=100)
    password_2=models.CharField(max_length=100)

    def __str__(self):
        return "{username}"
    
    def __str__(self):
        return "{email}"
    
    def __str__(self):
        return "{password_1}"
    
    def __str__(self):
        return "{password_2}"
    
    
class LoginModel(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self) -> str:
        return '{self.username}'
    
    def __str__(self) -> str:
        return '{self.password}'
    