from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("fill_form", views.fill_form),
    path("register", views.register),
    path('search_patient', views.search_patient),
    path('get_patient_details', views.get_patient_details)
    ]
