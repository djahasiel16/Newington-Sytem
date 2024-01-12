from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import SurigaoRequestHeader, SurigaoRequestItems
from .forms import SurigaoRequestHeaderForm
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'surigao_requests/home.html')


def add_request_view(request):
    if request.method == 'POST':
        form = SurigaoRequestHeaderForm(request.POST, instance=SurigaoRequestHeader(user=User.objects.get(pk=request.user.id)))
        if form.is_valid:
            form.save()
            return HttpResponse("Saved Successfully")
        
    rs_number = f"SRGO{timezone.now().year}-"
    
    try:
        idx = SurigaoRequestHeader.objects.last()
        rs_number += str(idx.id+1).zfill(3)
    except:
        rs_number += str(1).zfill(3)

    form = SurigaoRequestHeaderForm(initial={'rs_number':rs_number})
    return render(request, 'surigao_requests/add_request.html', {'form':form})