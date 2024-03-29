"""
URL configuration for requisition_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('davao/', include('davao_requests.urls')),
    path('surigao/', include('surigao_requests.urls')),
    path('cotabato/', include('cotabato_requests.urls')),
    path('negros/', include('negros_requests.urls')),
    path('bukidnon/', include('bukidnon_requests.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('authentication.urls')),
    path('sys-settings/', include('sys_settings.urls')),
    re_path(r'^.*/$', views.home),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
