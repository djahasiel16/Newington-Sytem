from django.urls import path
from davao_requests import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personnel/', views.list_view_personnel, name='personnel_view'),
    path('save_personnel/', views.save_personnel_data, name='save_personnel')

]