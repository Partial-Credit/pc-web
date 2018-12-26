from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.media, name='media'),
    path('manage_songs', views.manage_songs, name='manage_songs')
]