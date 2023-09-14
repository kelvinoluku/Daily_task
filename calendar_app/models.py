from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    task = models.TextField()
    date_due = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
    
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
