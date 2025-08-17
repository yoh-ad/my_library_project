from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def checkout(self, request, pk=None):
        book = self.get_object()
        if book.is_checked_out:
            return Response({'error': 'Book already checked out'}, status=status.HTTP_400_BAD_REQUEST)
        book.is_checked_out = True
        book.checked_out_by = request.user
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def return_book(self, request, pk=None):
        book = self.get_object()
        if book.checked_out_by != request.user:
            return Response({'error': 'You cannot return this book'}, status=status.HTTP_400_BAD_REQUEST)
        book.is_checked_out = False
        book.checked_out_by = None
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)
