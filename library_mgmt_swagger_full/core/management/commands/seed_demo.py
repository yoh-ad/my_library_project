from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.conf import settings
from core.models import Book

class Command(BaseCommand):
    help = "Seed demo groups, users, and a sample book"

    def handle(self, *args, **options):
        librarian_group, _ = Group.objects.get_or_create(name=settings.LIBRARIAN_GROUP)
        member_group, _ = Group.objects.get_or_create(name=settings.MEMBER_GROUP)

        # Librarian
        if not User.objects.filter(username='librarian').exists():
            u = User.objects.create_user('librarian', password='librarian123')
            u.groups.add(librarian_group)
            self.stdout.write(self.style.SUCCESS("Created librarian user: librarian / librarian123"))
        else:
            self.stdout.write("Librarian user exists")

        # Member
        if not User.objects.filter(username='member').exists():
            u = User.objects.create_user('member', password='member123')
            u.groups.add(member_group)
            self.stdout.write(self.style.SUCCESS("Created member user: member / member123"))
        else:
            self.stdout.write("Member user exists")

        # Sample Book
        if not Book.objects.filter(isbn='ISBN-0001').exists():
            Book.objects.create(
                title='Django 101', author='Jane Doe', category='Tech',
                description='Intro to Django', isbn='ISBN-0001',
                total_copies=3, available_copies=3
            )
            self.stdout.write(self.style.SUCCESS("Created sample book: Django 101"))
        else:
            self.stdout.write("Sample book exists")

        self.stdout.write(self.style.SUCCESS("Seeding complete."))
