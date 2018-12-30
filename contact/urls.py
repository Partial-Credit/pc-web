from django.contrib import admin
from django.urls import path, include # new
from . import views

app_name = 'contact'

urlpatterns = [
    path('email/', views.emailView, name = 'email'), # new
    path('success/', views.successView, name = 'success'),
]