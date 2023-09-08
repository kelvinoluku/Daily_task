from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='calendar-home'),
    path('tasks/', views.tasks, name='calendar-tasks'),
]
