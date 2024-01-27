from django.urls import path
from davao_requests import views

print("main urls is accessed")

urlpatterns = [
    path('', views.dashboard, name='davao'),
    # path('add_request/', views.add_request_view, name='davao_add_request'),
    # path('add_items/<rs_number>/', views.add_items_view, name='davao_add_items'),
    # #Unused URLS
    # path('rsSlip/<rs_number>/', views.rs_view, name='rsView'),
    # path('add_authorizedPerson/<rs_number>/', views.add_authorizedPerson_view, name='davao_add_authorizedPerson'),
    # path('list_view_request/', views.list_view_requests, name='davao_list_view_requests'),
    # path('edit_authorizedPerson/<rs_number>/', views.edit_authorizedPerson_view, name='davao_edit_authorizedPerson'),
    # path('edit_item/<rs_id>/', views.edit_item_view, name='davao_edit_item_view'),
    # path('edit_request/<rs_number>/', views.edit_request_view, name='davao_edit_request_view'),
    # path('list_view_items/', views.list_view_items, name='davao_list_view_items'),
    # path('go_back/', views.go_back, name='go-back'),
    # path('delete_item/<item_id>/', views.delete_item, name='davao_delete_item')

]