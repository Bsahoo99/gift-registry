# Django Gift Registry

A Django gift registry with custom session-based authentication and template inheritance.

## Overview

Users register and log in through a manual session-based auth system — there is no Django built-in `User` model or `@login_required`. Authentication state is tracked via `request.session['user_id']`; views redirect to an error page if the key is missing. Each user can manage their own gift list and browse other users' gifts. All page templates extend a shared `base.html` that provides the navigation bar. Passwords are stored in plaintext in the database — this is intentional for a demo only.

## Requirements

- Python 3.10+
- Django 5.0

## Project Structure

```
gift-registry/
├── manage.py
├── pyproject.toml
├── poetry.lock
├── .gitignore
├── README.md
└── django_project/
    ├── __init__.py
    ├── asgi.py
    ├── admin.py
    ├── models.py           # MyUser and Gift models
    ├── settings.py
    ├── urls.py
    ├── views.py            # FBVs for auth, gifts, and user browsing
    ├── wsgi.py
    ├── templates/
    │   ├── base.html       # Shared layout with nav
    │   ├── home.html
    │   ├── login.html
    │   ├── registration.html
    │   ├── gifts.html
    │   ├── users.html
    │   ├── other_users_gifts.html
    │   └── error.html
    └── migrations/
        ├── __init__.py
        └── 0001_initial.py
```

## Usage

```bash
poetry install
python manage.py migrate
python manage.py runserver
```

Register a new account at `http://127.0.0.1:8000/registration/`, then log in at `/login/`.

## Key Files

| File | What it does |
|------|--------------|
| `manage.py` | Django project entry point |
| `django_project/models.py` | `MyUser` (plaintext password) and `Gift` (FK to MyUser) |
| `django_project/views.py` | Manual session auth, gift CRUD, and user-browsing views |
| `django_project/urls.py` | Routes for login, registration, gifts, users, and error |
| `django_project/templates/base.html` | Shared base template with navigation bar |
| `django_project/templates/gifts.html` | Current user's gift list |

## Author

Biswajeet Sahoo

## License

MIT License
