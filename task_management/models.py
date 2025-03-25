from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    '''
    Attributes:
        name (str): The title of the task.
        description (str): A detailed explanation of the task.
        created_at (datetime): The timestamp when the task was created.(optional)
        task_type (str): The category or type of the task.(optional)
        completed_at (datetime, optional): The timestamp when the task was completed.(optional)
        status (str): The current status of the task. Defaults to 'Pending'.(optional)
        assigned_users (ManyToManyField): The users assigned to the task.
    '''
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')
    assigned_users = models.ManyToManyField(User, related_name='tasks')
