from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth.models import auth, User
from django.contrib import messages

from .models import BlogPost
from .forms import BlogForm
# Create your views here.


def register(request):
    if request.method=="POST":

        username=request.POST.get('username', ' ')
        email=request.POST.get('email', ' ')
        password_1=request.POST.get('password1', ' ')
        password_2=request.POST.get('password2', ' ')
        
        if password_1 == password_2:
            if len(password_1) > 10 and len(password_2) > 10:

                if User.objects.filter(username=username).exists():
                    messages.info(request, f"This username {username} is already in use!")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, f"The email {email} is already in use!")
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username, email=email, password=password_1)
                    user.save();

                    #TO DO: Create email notification logic

                    return redirect('login')

            else:
                messages.info(request, 'This Password is too short')
                return redirect('register')
        else:
            messages.info(request, "These passwords are not the same!")
            return redirect('register')
    
    return render(request, 'register.html')


def login(request):
    if request.method=="POST":
        username=request.POST.get("username", ' ')
        password=request.POST.get("password", ' ')
        is_authenticated=bool

        user=auth.authenticate(username=username, password=password)
        
        if user is not None:
            
            context={
                'username':username,
                is_authenticated:True,
            }

            auth.login(request, user)
            return render(request, 'index.html', context)
        
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
            return redirect("user's_post")
    else:
        form=BlogForm()
        return render(request, "user's_post.html", {"form":form})