# Task Backend

A Django-based backend project.

## Setup Instructions

1. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start development server:

```bash
python manage.py runserver
```

The server will run at http://127.0.0.1:8000/

## endpoints

api/v1/auth/login/ - login
api/v1/auth/register/ - signup
api/v1/tasks/ - list and create
api/v1/tasks/:id/ - delete/update
api/v1/tasks/dashboard-count/ - dashboard
