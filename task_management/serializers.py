from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    '''
    Serializer for the User model.
    This serializer converts User model instances into JSON representations
    and specifies the fields to be included in API responses.
    '''
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TaskSerializer(serializers.ModelSerializer):
    '''
    Serializer for the Task model.

    - Includes all fields of the Task model.
    - Displays assigned users as nested user objects using `UserSerializer`.
    - The `assigned_users` field is read-only to prevent modifications during task creation/update.
    '''
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
