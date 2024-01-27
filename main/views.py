from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'main/dashboard.html')


def dynamic_url(request):
    try:
        url = request.META['HTTP_REFERER']
        url = '/'.join(url.split('/')[2:4])
        
    except:
        pass