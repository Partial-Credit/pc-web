from django.urls import path, re_path
from . import views

from django.contrib.auth.decorators import login_required, permission_required

app_name = 'music'

urlpatterns = [
    path('', views.media, name='media'),
    path('manage_songs', permission_required('users.officer', raise_exception=True)(views.SongCreate.as_view()), name='manage_songs'),
    path('manage_albums', permission_required('users.officer', raise_exception=True)(views.AlbumCreate.as_view()), name='manage_albums'),
    path('edit_songs', views.edit_songs, name='edit_songs'),
    re_path(r'^edit_songs/(?P<pk>\d+)/$', permission_required('users.officer', raise_exception=True)(views.SongUpdate.as_view()), name ="edit_song"),
    re_path(r'^edit_songs/delete/(?P<pk>\d+)/$', permission_required('users.officer', raise_exception=True)(views.SongDelete.as_view()), name ="delete_song"),
    path('edit_albums', views.edit_albums, name='edit_albums'),
    re_path(r'^edit_albums/(?P<pk>\d+)/$',permission_required('users.officer', raise_exception=True)(views.AlbumUpdate.as_view()), name ="edit_album"),
    re_path(r'^edit_albums/delete/(?P<pk>\d+)/$', permission_required('users.officer', raise_exception=True)(views.AlbumDelete.as_view()), name ="delete_album")
]
