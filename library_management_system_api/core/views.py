from datetime import timedelta
from django.utils import timezone

from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Book, Borrow
from .serializers import BookSerializer, BorrowSerializer
from .permissions import IsLibrarianOrReadOnly, IsMember

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated & IsLibrarianOrReadOnly]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'author', 'isbn', 'category']
    ordering_fields = ['title', 'author', 'created_at']

class BorrowViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Borrow.objects.select_related('book', 'user').all()
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticated & IsMember]
    filterset_fields = ['book', 'borrowed_at', 'due_at', 'returned_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.validated_data['book']
        if book.available_copies <= 0:
            return Response({'detail': 'No copies available.'}, status=400)
        due_at = serializer.validated_data.get('due_at') or timezone.now() + timedelta(days=14)
        book.available_copies -= 1
        book.save(update_fields=['available_copies'])
        serializer.save(user=request.user, due_at=due_at)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'], url_path='return_')
    def return_(self, request, pk=None):
        borrow = self.get_object()
        if not (request.user.is_staff or borrow.user == request.user):
            return Response({'detail': 'Not allowed.'}, status=403)
        if borrow.returned_at:
            return Response({'detail': 'Already returned.'}, status=400)
        borrow.mark_returned()
        return Response({'status': 'returned'})
