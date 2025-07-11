# todo/urls.py
from django.urls import path
from . import views
from .views import run_migrations

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('run-migrations/', run_migrations),
]
