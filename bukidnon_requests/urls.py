from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='bukidnon'),
    path('add_request/', views.add_request_view, name='bukidnon_add_request'),
    path('add_items/<rs_number>/', views.add_items_view, name='bukidnon_add_items'),
    path('addRequest_items/<rs_number>/', views.add_itemsRequest_view, name='bukidnon_addRequest_items'),
    path('rsSlip/<rs_number>/', views.rs_view, name='bukidnon_rsView'),
    path('add_authorizedPerson/<rs_number>/', views.add_authorizedPerson_view, name='bukidnon_add_authorizedPerson'),
    path('list_view_persons/', views.list_view_persons, name='bukidnon_list_view_persons'),
    path('list_view_request/', views.list_view_requests, name='bukidnon_list_view_requests'),
    path('edit_authorizedPerson/<person_id>/', views.edit_authorizedPerson_view, name='bukidnon_edit_authorizedPerson'),
    path('delete_person/<person_id>', views.delete_person, name='bukidnon_delete_person'),
    path('edit_item/<rs_id>/', views.edit_item_view, name='bukidnon_edit_item_view'),
    path('edit_request/<rs_number>/', views.edit_request_view, name='bukidnon_edit_request_view'),
    path('list_view_items/', views.list_view_items, name='bukidnon_list_view_items'),
    path('list_viewRequest_items/<rs_number>/', views.list_viewRequest_items, name='bukidnon_list_viewRequest_items'),
    path('go_back/', views.go_back, name='go-back'),
    path('delete_item/<item_id>/', views.delete_item, name='bukidnon_delete_item'),
    path('delete_request/<rs_number>/', views.delete_request, name='bukidnon_delete_request'),
    path('list_view_reports/', views.list_view_report, name='list_view_reports'),
    path('monitoringForm/', views.monitoringForm, name='get_items_data')
]