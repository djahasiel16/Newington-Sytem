from django.urls import path
from davao_requests import views
from . import views

urlpatterns = [
    path('', views.home, name='home')

]