from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth.models import auth, User
from django.contrib import messages

from .models import BlogPost, LoginModel
from .forms import BlogForm, RegisterForm 
# Create your views here.


def register(request):
    if request.method=="POST":

        register_form=RegisterForm(request.POST)
        
        if register_form.password_1 == register_form.password_2:
            if len(register_form.password_1) > 10 and len(register_form.password_2) > 10:

                if User.objects.filter(username=register_form.username).exists():
                    messages.info(request, f"This username {register_form.username} is already in use!")
                    return redirect('register')
                elif User.objects.filter(email=register_form.email).exists():
                    messages.info(request, f"The email {register_form.email} is already in use!")
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=register_form.username, email=register_form.email, password=register_form.password_1)
                    user.save();

                    #TO DO: Create email notification logic

                    return redirect('login')

            else:
                messages.info(request, 'This Password is too short')
                return redirect('register')
        else:
            messages.info(request, "These passwords are not the same!")
            return redirect('register')
    else:
        register_form=RegisterForm()
        return render(request, 'register.html', {"register_form":register_form})


def login(request):
    if request.method=="POST":
        Login_form=LoginModel(request.POST)

        if Login_form.is_valid():

            auth.login(request, Login_form.cleaned_data['user'])
            username=Login_form.cleaned_data["username"]
            
            return render(request, 'index.html', {'username':username})
        
        else:
            messages.info(request, 'Your credentials are incorrect!')
            return redirect('login')

    return render (request, "login.html")




def index(request):
    index_posts=BlogPost.objects.all()
    return render(request, 'index.html', {"index_posts":index_posts})


def post(request, pk):
    individual_post=BlogPost.objects.get(id=pk)
    return render(request, 'posts.html', {"ind_post":individual_post})


def user_post(request):
    #View for saving user input to database
    if request.method=="POST":
        form=BlogForm(request.POST)

        if form: #To check if it is empty
            if form.is_valid():
                form.save();
                return redirect('index')
        else:
            messages.info(request, 'The blog post is not valid!')
            return redirect("users_post")
    else:
        form=BlogForm()
        return render(request, "users_post.html", {"form":form})