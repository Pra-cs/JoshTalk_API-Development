import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management_api.settings')

# Get the WSGI application instance for serving the project
application = get_wsgi_application()
