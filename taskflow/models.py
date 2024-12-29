from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Each task is related to a specific user
    title = models.CharField(max_length=200)  # Task description
    completed = models.BooleanField(default=False)  # Mark the task as completed or not
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the task was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the task was last updated

    def __str__(self):
        return self.title
