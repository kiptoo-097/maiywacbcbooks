from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, UserRequest
from django.contrib import messages
from .forms import UserRequestForm
from django.contrib.auth.decorators import login_required

def home(request):
    books = Book.objects.all()
    user_requests = UserRequest.objects.filter(user=request.user) if request.user.is_authenticated else []
    requests_dict = {user_request.book.id: user_request for user_request in user_requests}
    return render(request, 'bookstore/home.html', {'books': books, 'requests_dict': requests_dict})

def about(request):
    return render(request, 'bookstore/about.html', )

def videos(request):
    return render(request, 'bookstore/videos.html') 

@login_required
def profile(request):
    user_requests = UserRequest.objects.filter(user=request.user)
    return render(request, 'bookstore/profile.html', {'user_requests': user_requests})

@login_required
def book_request(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    existing_request = UserRequest.objects.filter(user=request.user, book=book).first()

    if existing_request:
        if existing_request.approved:
            messages.info(request, "You already have access to this book.")
            return redirect('profile')
        else:
            messages.info(request, "Your request is pending approval.")
            return redirect('profile')
    
    if request.method == 'POST':
        form = UserRequestForm(request.POST)
        if form.is_valid():
            user_request = form.save(commit=False)
            user_request.user = request.user
            user_request.book = book
            user_request.save()
            messages.success(request, "Access request submitted. Please wait for approval.")
            return redirect('profile')
    else:
        form = UserRequestForm()
    return render(request, 'bookstore/book_request.html', {'form': form, 'book': book})

@login_required
def read_book(request, book_id):
    user_request = get_object_or_404(UserRequest, book_id=book_id, user=request.user)
    if user_request.approved:
        book = user_request.book
        return render(request, 'bookstore/read_book.html', {'book': book})
    messages.warning(request, "Access not yet approved.")
    return redirect('profile')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'bookstore/register.html', {'form': form})

# bookstore/views.py
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next') or 'home'  # Use 'next' if available, else default to 'home'
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'bookstore/login.html', {'form': form})


def books(request):
    # Query all books from the database
    books = Book.objects.all()

    # Render the books.html template and pass the books
    return render(request, 'bookstore/books.html', {'books': books})

def contact_view(request):
    return render(request, 'bookstore/contact.html')