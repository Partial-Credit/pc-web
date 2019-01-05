from django.urls import path, re_path
from . import views

app_name = "home"
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('media/add_photos', views.PhotoCreate.as_view(), name="manage_photos"),
    path('media/edit_photos', views.edit_photos, name='edit_photos'),
    re_path(r'^media/edit_photos/(?P<pk>\d+)/$',views.PhotoUpdate.as_view(), name ="edit_photos"),
    re_path(r'^media/edit_photos/delete/(?P<pk>\d+)/$',views.PhotoDelete.as_view(), name ="delete_photos"),
]
