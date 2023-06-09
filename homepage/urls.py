from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_home_page),
    path("signup", views.signup),
    path('login', views.login),
    path('user_login', views.user_login),
    path('logout', views.logout)
]
