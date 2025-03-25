from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Initialize router and register TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include all router-generated URLs
]
