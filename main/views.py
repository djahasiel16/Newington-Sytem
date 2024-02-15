from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        # return render(request, 'main/home.html')
        return redirect(reverse('davao'))
    else:
        return redirect('login')
