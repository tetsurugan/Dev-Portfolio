from django.db import models  # Import Django's built-in ORM model functionality
from django.contrib.auth.models import User  # Import Django's built-in user authentication model

class Task(models.Model):  # Defines a database model for a to-do list item
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    # Links each task to a user (tasks belong to a specific user).
    # If a user is deleted, all their tasks are deleted as well (CASCADE behavior).

    title = models.CharField(max_length=255)  
    # Title of the task (short string, max 255 characters)

    description = models.TextField(blank=True, null=True)  
    # Optional longer text field for details about the task.

    due_date = models.DateField(blank=True, null=True)  
    # Stores the due date of the task (optional field).

    completed = models.BooleanField(default=False)  
    # True/False field to track whether the task is completed.

    created_at = models.DateTimeField(auto_now_add=True)  
    # Automatically records when the task was created.

    def __str__(self):  
        # Determines how the task is displayed (shows title when printed)
        return self.title