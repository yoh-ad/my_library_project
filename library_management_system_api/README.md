# Library Management System API

A clean starter for your BE Capstone, built with **Django 5** + **DRF** + **SimpleJWT**.

## Features
- JWT Authentication (access/refresh)
- Role-based permissions (Admin, Librarian, Member)
- Books CRUD
- Borrow & Return flow
- Filtering and searching
- SQLite by default (easy to run locally)

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### API Endpoints (prefix `/api/`)
- `POST /api/auth/token/` — obtain JWT
- `POST /api/auth/token/refresh/` — refresh JWT
- `GET/POST /api/books/` — list/create (Librarian/Admin create)
- `GET/PUT/PATCH/DELETE /api/books/{id}/`
- `GET/POST /api/borrows/` — list/create borrow (Members create)
- `POST /api/borrows/{id}/return_/` — return a borrowed book

### Roles
- **Admin**: full access
- **Librarian**: manage books, view borrows
- **Member**: browse books, borrow & return own

## Project Tree
```
library_management_system_api/
├─ manage.py
├─ requirements.txt
├─ README.md
├─ .env.example
├─ library_api/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
└─ core/
   ├─ __init__.py
   ├─ admin.py
   ├─ apps.py
   ├─ models.py
   ├─ serializers.py
   ├─ permissions.py
   ├─ views.py
   ├─ urls.py
   ├─ tests.py
   └─ migrations/
      └─ __init__.py

```
