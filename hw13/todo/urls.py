from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.todo_add, name='todo_add'),
    path('toggle/<int:pk>/', views.todo_toggle, name='todo_toggle'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
]