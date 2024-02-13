from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='negros'),
    path('add_request/', views.add_request_view, name='negros_add_request'),
    path('add_items/<rs_number>/', views.add_items_view, name='negros_add_items'),
    #Unused URLS
    path('rsSlip/<rs_number>/', views.rs_view, name='negros_rsView'),
    path('add_authorizedPerson/<rs_number>/', views.add_authorizedPerson_view, name='negros_add_authorizedPerson'),
    path('list_view_request/', views.list_view_requests, name='negros_list_view_requests'),
    path('edit_authorizedPerson/<rs_number>/', views.edit_authorizedPerson_view, name='negros_edit_authorizedPerson'),
    path('edit_item/<rs_id>/', views.edit_item_view, name='negros_edit_item_view'),
    path('edit_request/<rs_number>/', views.edit_request_view, name='negros_edit_request_view'),
    path('list_view_items/', views.list_view_items, name='negros_list_view_items'),
    path('go_back/', views.go_back, name='negros_go-back'),
    path('delete_item/<item_id>/', views.delete_item, name='negros_delete_item')

]