from rest_framework import serializers
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import Book, Borrow

User = get_user_model()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'description', 'isbn',
                  'total_copies', 'available_copies', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'available_copies']

class BorrowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    book_title = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = Borrow
        fields = ['id', 'user', 'book', 'book_title', 'borrowed_at', 'due_at', 'returned_at']
        read_only_fields = ['id', 'borrowed_at', 'returned_at']

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True, slug_field='name', queryset=Group.objects.all()
    )
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']
