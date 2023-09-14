from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Post
from datetime import date


@login_required
def home(request):
    context = {
        'posts': Post.objects.all(),
        'filtered_posts': Post.objects.filter(date_due=date.today())
    }
    return render(request, 'calendar_app/home.html', context)


class TaskListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'calendar_app/tasks.html'
    context_object_name = 'posts'
    ordering = ['date_due']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtered_posts'] = Post.objects.filter(date_due=date.today())
        return context


class TaskDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtered_posts'] = Post.objects.filter(date_due=date.today())
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['task', 'date_due']
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtered_posts'] = Post.objects.filter(date_due=date.today())
        return context

    
class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['task', 'date_due']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/tasks/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
