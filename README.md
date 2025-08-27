Library Management System API
Project Overview

The Library Management System API is a Django-based application that allows libraries to manage books, users, and borrow/return operations.
It provides a RESTful API with authentication, role-based access (librarian vs member), and interactive API documentation via Swagger and ReDoc.

This project was built as part of the ALX Back-End Web Development Capstone Project.

Features

User Roles

Librarian: Can create, update, and delete books.

Member: Can borrow and return books.

Book Management

Add, view, and list books.

Borrow and return books with proper validation.

Authentication

JWT-based login and token refresh.

Role-based permissions for different actions.

API Documentation

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/

Demo Users
Role	Username	Password
Librarian	librarian	librarian123
Member	member	member123
Installation & Setup

Clone the repository

git clone <YOUR_GITHUB_REPO_URL>
cd library_mgmt_swagger_full/library_mgmt_swagger_full


Create a virtual environment

python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash


Install dependencies

pip install -r requirements.txt


Create migrations and migrate

python manage.py makemigrations core
python manage.py migrate


Seed demo data

python manage.py seed_demo


Run the server

python manage.py runserver 0.0.0.0:8000

How to Test

Open Swagger UI: http://127.0.0.1:8000/swagger/

Log in with a demo user (librarian or member) using /api/auth/token/.

Try key operations:

Add, update, or delete books (librarian).

Borrow or return books (member).

Notes

This project is for educational purposes and runs on Django’s development server.

Not intended for production use.

Author

Yohannes Adugna
ALX Back-End Web Development Capstone Project
