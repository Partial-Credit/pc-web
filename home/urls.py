from django.urls import path, re_path
from . import views

app_name = "home"
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dashboard/add_photos', views.PhotoCreate.as_view(), name="manage_photos"),
    path('dashboard/edit_photos', views.edit_photos, name='edit_photos'),
    re_path(r'^dashboard/edit_photos/(?P<pk>\d+)/$',views.PhotoUpdate.as_view(), name ="edit_photos"),
    re_path(r'^dashboard/edit_photos/delete/(?P<pk>\d+)/$',views.PhotoDelete.as_view(), name ="delete_photos"),
    path('dashboard/add_articles', views.ArticleCreate.as_view(), name="manage_articles"),
    path('dashboard/edit_articles', views.edit_articles, name='edit_articles'),
    path('dashboard/edit_articles/<str:slug>/',views.ArticleUpdate.as_view(), name ="edit_article"),
    path('dashboard/edit_articles/delete/<str:slug>/',views.ArticleDelete.as_view(), name ="delete_articles"),
]
