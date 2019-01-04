from django.urls import path
from . import views

app_name = "auditions"
urlpatterns = [
    path('', views.audition, name='audition'),
]