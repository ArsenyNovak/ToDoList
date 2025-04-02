from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('updateTask/<int:task_pk>/', views.UpdateTask.as_view(), name='update_task'),
    path('deleteTask/<int:task_pk>/', views.DeleteTask.as_view(), name='delete_task'),
    path('futureTasks/', views.FuturePage.as_view(), name='future_tasks'),
    path('archiveTasks/', views.ArchvePage.as_view(), name='archive_tasks'),
    path('runningTask/<int:task_pk>/', views.RunningTask.as_view(), name='running_task'),
]