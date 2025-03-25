from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    '''
    Managing tasks.
    - Allows CRUD operations on tasks.
    - Task assignment and retrieval by user.
    '''

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['post'])
    def assign(self, request, pk=None):
        '''
        Assign a task to multiple users.

        - Accepts a list of user IDs in the request body.
        - Validates user IDs and assigns them to the specified task.
        '''

        task = self.get_object()
        user_ids = request.data.get('users', [])

        if not user_ids or not isinstance(user_ids, list):
            return Response(
                {"error": "A list of user IDs is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        valid_users = User.objects.filter(id__in=user_ids)
        if len(valid_users) != len(user_ids):
            return Response(
                {"error": "One or more user IDs are invalid."},
                status=status.HTTP_400_BAD_REQUEST
            )

        task.assigned_users.set(valid_users)  # Assign users properly
        return Response({'message': 'Task assigned successfully'})

    @action(detail=False, methods=['get'])
    def user_tasks(self, request):
        '''
        Retrieve tasks assigned to a specific user.

        - Requires 'user_id' as a query.
        - Returns a list of tasks assigned to the user.
        '''

        user_id = request.query_params.get('user_id')

        if not user_id:
            return Response(
                {'error': 'User ID is required in query parameters.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user_id = int(user_id)  # Convert to integer to avoid errors
        except ValueError:
            return Response(
                {'error': 'Invalid user ID. It must be a number.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        tasks = Task.objects.filter(assigned_users__id=user_id)
        serializer = self.get_serializer(tasks, many=True)

        return Response({
            "message": "Tasks retrieved successfully.",
            "tasks": serializer.data
        })
