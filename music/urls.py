from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.media, name='media'),
    path('manage_songs', views.SongCreate.as_view(), name='manage_songs'),
    path('manage_albums', views.AlbumCreate.as_view(), name='manage_albums'),
    path('edit_songs', views.edit_songs, name='edit_songs'),
    re_path(r'^edit_songs/(?P<pk>\d+)/$',views.SongUpdate.as_view(), name ="edit_song"),
    re_path(r'^edit_songs/delete/(?P<pk>\d+)/$',views.SongDelete.as_view(), name ="delete_song"),
    path('edit_albums', views.edit_albums, name='edit_albums'),
    re_path(r'^edit_albums/(?P<pk>\d+)/$',views.AlbumUpdate.as_view(), name ="edit_album"),
    re_path(r'^edit_albums/delete/(?P<pk>\d+)/$',views.AlbumDelete.as_view(), name ="delete_album")
]