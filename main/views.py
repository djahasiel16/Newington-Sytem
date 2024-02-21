from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Personnel
from .forms import PersonnelForm
from django.contrib import messages
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        # return render(request, 'main/home.html')
        return redirect(reverse('davao'))
    else:
        return redirect('login')


def add_personnel_view(request):
    pass

def list_view_personnel(request):
    personnel = Personnel.objects.all()
    return render(request, 'main/actions/list_viewPersonnel.html', {'personnel':personnel, 'title':'Select Location'})

def save_personnel_data(request):
    if request.method == 'POST':
       
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personnel Addedd Successfully')
            
    return redirect(reverse('personnel_view'))

