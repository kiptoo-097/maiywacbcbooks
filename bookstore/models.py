# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    pdf = models.FileField(upload_to='books_pdfs/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class UserRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    request_message = models.TextField(blank=True)

    class Meta:
        unique_together = ('user', 'book')  # Prevent duplicate requests

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
