# bookstore/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                      # Homepage
    path('videos/', views.videos, name='videos'),
    path('profile/', views.profile, name='profile'),        # User's profile
    path('about/', views.about, name='about'),
    path('book_request/<int:book_id>/', views.book_request, name='book_request'),  # Book request page
    path('read_book/<int:book_id>/', views.read_book, name='read_book'),  # Read the book after approval
    path('login/', views.custom_login, name='login'),  # Custom login view
    path('register/', views.register, name='register'),  # Register page
    path('books/',views.books, name='books'),
    path('contact/', views.contact_view, name='contact'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)