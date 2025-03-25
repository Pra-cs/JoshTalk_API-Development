#!/usr/bin/env python
"""
API Development in Django/Python - For Josh Talks
"""
import os
import sys
'''

'''
if __name__ == "__main__":
    # Set the default Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_management_api.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Ensure it's installed and available on PYTHONPATH.") from exc
    execute_from_command_line(sys.argv)
