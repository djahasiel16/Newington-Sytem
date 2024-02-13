from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username, password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login Success')
        else:
            return HttpResponse('Login Failed')
    else:
        return render(request, 'registration/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login')



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {'form':form})