from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='surigao'),
    path('add_request/', views.add_request_view, name='surigao_add_request'),
]