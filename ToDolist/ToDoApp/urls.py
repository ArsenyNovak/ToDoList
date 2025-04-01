from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    # path('newTask/', views.CreateTask.as_view(), name='create_task'),
    # path('updateTask/<int:task_pk>/', views.UpdateTask.as_view(), name='update_task'),
    path('deleteTask/<int:task_pk>/', views.deletetask, name='delete_task'),
]