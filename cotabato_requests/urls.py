from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cotabato'),
    path('add_request/', views.add_request_view, name='cotabato_add_request'),
]