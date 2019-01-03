from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('media/add_photos', views.photo_list, name="manage_photos")
]
