from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('truck_control', views.truck_control, name='truck_control'),
    path('delivery_note', views.delivery_note, name='delivery_note'),
    path('generate/truck_control/', views.truck_control_pdf, name='truck_control_pdf'),
    path('generate/delivery_note/', views.delivery_note_pdf, name='delivery_note_pdf'),
    path('generate/index/', views.index_pdf, name='index_pdf'),
]