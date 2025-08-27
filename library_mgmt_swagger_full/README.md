# Library Management System API (Django + DRF + Swagger)

Ready-to-run capstone backend with:
- JWT auth (SimpleJWT)
- Roles via Groups (**Librarian**, **Member**)
- Books CRUD
- Borrow/Return flow
- Swagger UI & Redoc docs
- Auto-seeded demo users & sample data

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_demo   # creates groups/users and a sample book
python manage.py runserver
```

### Demo Accounts
- Librarian: `librarian` / `librarian123`
- Member: `member` / `member123`

### Docs
- Swagger: http://127.0.0.1:8000/swagger/
- Redoc:   http://127.0.0.1:8000/redoc/

### API (prefix `/api/`)
- `POST /api/auth/token/` — obtain JWT
- `POST /api/auth/token/refresh/` — refresh JWT
- `GET/POST /api/books/` — list/create (Librarian/Admin create)
- `GET/PUT/PATCH/DELETE /api/books/{id}/`
- `GET/POST /api/borrows/` — list/create borrow (Members create)
- `POST /api/borrows/{id}/return_/` — return a borrowed book

## Project Tree
```
library_mgmt_swagger_full/
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
   ├─ migrations/
   │  └─ __init__.py
   └─ management/
      └─ commands/
         └─ seed_demo.py

```
