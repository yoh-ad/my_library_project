from django.contrib import admin
from .models import Book, Borrow

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'available_copies', 'total_copies')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category',)

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'borrowed_at', 'due_at', 'returned_at')
    list_filter = ('borrowed_at', 'due_at', 'returned_at')
    search_fields = ('user__username', 'book__title')
