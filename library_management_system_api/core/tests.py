from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group
from rest_framework import status
from core.models import Book

class BasicFlowTest(APITestCase):
    def setUp(self):
        self.librarian_group, _ = Group.objects.get_or_create(name='Librarian')
        self.member_group, _ = Group.objects.get_or_create(name='Member')
        self.admin = User.objects.create_superuser('admin', 'admin@test.com', 'pass1234')
        self.librarian = User.objects.create_user('lib', 'lib@test.com', 'pass1234')
        self.librarian.groups.add(self.librarian_group)
        self.member = User.objects.create_user('mem', 'mem@test.com', 'pass1234')
        self.member.groups.add(self.member_group)
        self.book = Book.objects.create(title='Django 101', author='Jane', category='Tech',
                                        description='Intro', isbn='ISBN-0001', total_copies=2, available_copies=2)

    def test_book_requires_auth(self):
        res = self.client.get('/api/books/')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
