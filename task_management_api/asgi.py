import os
from django.core.asgi import get_asgi_application

# Set the default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management_api.settings')

# Get application instance
application = get_asgi_application()
