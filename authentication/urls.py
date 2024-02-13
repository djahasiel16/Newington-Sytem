from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path ('logout_user/', views.logout_user, name='logout_user'),
    path('register/', views.register, name='register'),
]