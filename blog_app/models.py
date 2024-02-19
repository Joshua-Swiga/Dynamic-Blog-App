from django.db import models

# Create your models here.
class BlogPost(models.Model):
    date=models.DateField(auto_now = True)
    title=models.CharField(max_length=100)
    body=models.TextField()

    def __str__(self) -> str:
        return f"{self.title}"


class RegisterModel(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password_1=models.CharField(max_length=100)
    password_2=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.username}, {self.email}, {self.password_1}, {self.password_2}"
    
class LoginModel(models.Model):
    username=models.CharField(max_length=100, blank=False)
    password=models.CharField(max_length=100, blank=False)

    def __str__(self) -> str:
        return '{self.username}'
    
    def __str__(self) -> str:
        return '{self.password}'
    
