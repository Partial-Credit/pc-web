from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view, name='users-view'),
    path('all/', views.viewAll, name='users-view-all'),
    path('all/<str:sort_by>', views.viewAll, name='users-view-all'),
    path('edit/<int:member_id>', views.edit, name='users-edit'),
    path('add/', views.add, name='users-add'),
    path('remove/', views.remove, name='users-remove'),

]
