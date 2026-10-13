from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Book

def landing_page(request):
    books = Book.objects.all()
    context = {
        'page_title': 'Welcome to Our Bookstore',
        'welcome_message': 'Discover your next great read. Browse our extensive collection of books and read authentic reviews.',
        'books': books,
        'current_year': timezone.now().year,
    }
    return render(request, 'books/index.html', context)

def book_list(request):
    books = Book.objects.all()
    context = {
        'page_title': 'All Books',
        'books': books,
        'current_year': timezone.now().year,
    }
    return render(request, 'books/book_list.html', context)

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {
        'page_title': book.title,
        'book': book,
        'current_year': timezone.now().year,
    }
    return render(request, 'books/book_details.html', context)
