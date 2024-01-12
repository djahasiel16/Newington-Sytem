from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='davao'),
    path('add_request/', views.add_request_view, name='davao_add_request'),
    path('add_items/<rs_number>/', views.add_items_view, name='davao_add_items'),
    #Unused URLS
    path('rsSlip/<rs_number>/', views.rs_view, name='rsView'),
    path('add_authorizedPerson/<rs_number>/', views.add_authorizedPerson_view, name='add_authorizedPerson'),
    path('list_view_request/', views.list_view_requests, name='list_view_requests'),
    path('edit_authorizedPerson/<rs_number>/', views.edit_authorizedPerson_view, name='edit_authorizedPerson'),
    path('edit_item_view/<rs_id>/', views.edit_item_view, name='edit_item_view'),
    path('list_view_items/', views.list_view_items, name='list_view_items'),
    path('go_back/', views.go_back, name='go-back'),
    path('delete_item/<item_id>/', views.delete_item, name='delete_item')

]