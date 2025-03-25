"""""""""""""""""""""""""""""""""""""""""""""""""""
API Development in Django/Python - For Josh Talks
"""""""""""""""""""""""""""""""""""""""""""""""""""

# Tech Stack

- Backend: Django, DRF
- Database: SQLite
- Authentication: Django default auth system
- Testing: Postman

# Prerequisites

Ensure you have the following installed:

- https://www.python.org/downloads/
- https://pip.pypa.io/en/stable/installation/

# Setup

1. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip3 install -r requirements.txt

3. Apply migrations and start the server:
   python manage.py migrate
   python manage.py runserver

# API Endpoints

- Create a Task: `POST /api/tasks/`
- Assign Users to a Task: `POST /api/tasks/{task_id}/assign/`
- Retrieve User's Tasks: `GET /api/tasks/user_tasks/?user_id=<user_id>`

# Contact

Email: iitg.prabhat@gmail.com
