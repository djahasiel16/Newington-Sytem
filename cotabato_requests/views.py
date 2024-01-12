from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import CotabatoRequestHeader, CotabatoRequestItems
from .forms import CotabatoRequestHeaderForm
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'Cotabato_requests/home.html')


def add_request_view(request):
    if request.method == 'POST':
        form = CotabatoRequestHeaderForm(request.POST, instance=CotabatoRequestHeader(user=User.objects.get(pk=request.user.id)))
        if form.is_valid:
            form.save()
            return HttpResponse("Saved Successfully")
    rs_number = f"CBT{timezone.now().year}-"
    try:
        idx = CotabatoRequestHeader.objects.last()
        rs_number += str(idx.id+1).zfill(3)
    except:
        rs_number += str(1).zfill(3)

    form = CotabatoRequestHeaderForm(initial={'rs_number':rs_number})
    return render(request, 'Cotabato_requests/add_request.html', {'form':form})