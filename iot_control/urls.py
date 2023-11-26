
from django.contrib import admin
from django.urls import path

from . import  views

urlpatterns = [
    path('', views.landing_page, name="index"),
    path('devices',views.device_list, name="devices"),
    path('devices_add', views.device_add, name="add"),
    path('devices_del/<str:id>', views.delete, name="delete"),
    path('devices_upd/<str:id>', views.update, name="update"),
]
