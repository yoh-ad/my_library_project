from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    is_checked_out = models.BooleanField(default=False)
    checked_out_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='borrowed_books')

    def __str__(self):
        return f"{self.title} by {self.author}"
