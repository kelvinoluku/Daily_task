from django.urls import path
from .views import (
    TaskListView, 
    TaskDetailView, 
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='calendar-home'),
    path('tasks/', TaskListView.as_view(), name='calendar-tasks'),
    path('post/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('post/new/', TaskCreateView.as_view(), name='task-create'),
    path('post/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('post/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
