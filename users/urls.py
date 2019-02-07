from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('all/', views.viewAll, name='view_all'),
    path('all/<str:sort_by>', views.viewAll, name='view_all'),
    path('edit/<int:member_id>', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('remove/<int:member_id>', views.remove, name='remove'),
    path('graduate/<int:member_id>', views.setAlumni, name='graduate')
]
