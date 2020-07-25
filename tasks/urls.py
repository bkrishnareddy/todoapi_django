from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskOverview, name="api-overview"),
    path('task-list/', views.taskList, name="Task-List"),
    path('task-detail/<str:pk>/', views.taskDetail, name="Task-Detail"),
    path('task-create/', views.taskCreate, name="Task-Create"),
    path('task-update/<str:pk>/', views.taskUpdate, name="Task-Update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="Task-Delete"),
]
