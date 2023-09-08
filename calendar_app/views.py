from django.shortcuts import render
from .models import Post

context = {
        'posts': Post.objects.all()
    }

def home(request):
    return render(request, 'calendar_app/home.html', context)

def tasks(request):
    return render(request, 'calendar_app/tasks.html', context)
