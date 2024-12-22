from django.urls import path
from . import views

urlpatterns = [
  
  path('', views.home, name='plants'),
  path('plant/create', views.create_plant, name='plant-create'),
  path('plant/edit/<int:id>/', views.edit_plant, name='plant-edit'),
  path('plant/delete/<int:id>/', views.delete_plant, name='plant-delete'),
]