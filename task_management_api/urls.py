from django.contrib import admin
from django.urls import path, include

'''
-  Admin panel URL
- API URLs
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('task_management.urls')),
]
