from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.media, name='media'),
    path('manage_songs', views.manage_songs, name='manage_songs'),
    path('edit_songs', views.edit_songs, name='edit_songs'),
    re_path(r'^edit_songs/(?P<pk>\d+)/$',views.SongUpdate.as_view(), name ="edit_song")
]