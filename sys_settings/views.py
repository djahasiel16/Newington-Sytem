from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'sys-settings/index.html', {'title':request.GET.get('title', 'Davao')})