from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='surigao'),
    path('add_request/', views.add_request_view, name='surigao_add_request'),
    path('add_items/<rs_number>/', views.add_items_view, name='surigao_add_items'),
    #Unused URLS
    path('rsSlip/<rs_number>/', views.rs_view, name='surigao_rsView'),
    path('add_authorizedPerson/<rs_number>/', views.add_authorizedPerson_view, name='surigao_add_authorizedPerson'),
    path('list_view_request/', views.list_view_requests, name='surigao_list_view_requests'),
    path('edit_authorizedPerson/<rs_number>/', views.edit_authorizedPerson_view, name='surigao_edit_authorizedPerson'),
    path('edit_item/<rs_id>/', views.edit_item_view, name='surigao_edit_item_view'),
    path('edit_request/<rs_number>/', views.edit_request_view, name='surigao_edit_request_view'),
    path('list_view_items/', views.list_view_items, name='surigao_list_view_items'),
    path('go_back/', views.go_back, name='surigao_go-back'),
    path('delete_item/<item_id>/', views.delete_item, name='surigao_delete_item')

]