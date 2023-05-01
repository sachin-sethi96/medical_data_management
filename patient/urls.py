from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("fill_form", views.fill_form),]
