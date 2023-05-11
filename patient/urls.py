from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("fill_form", views.fill_form),
    path("register", views.register),
    path('search_patient', views.search_patient),
    path('medicate/<str:registration_id>', views.medicate),
    path('save_medication/<str:registration_id>', views.save_medication)
    ]
