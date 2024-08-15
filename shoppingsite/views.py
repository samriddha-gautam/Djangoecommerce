from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from shoppingsite.models import User

# Create your views here.

def homepage(request):
    return render(request,'base.html')

@login_required(login_url='/signup/')

def mainpage(request):
    return render(request,'mainpage.html')

def contactUs(request):
    return render(request, 'contactUs.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def signup(request):
    return render(request, 'signuppage.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username'],
        email = request.POST['email'],
        password = request.POST['password']
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    user = login(username=username,password=password)
    return redirect("mainpage")