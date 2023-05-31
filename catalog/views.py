from django.shortcuts import render
from catalog.models import Book, Author
# Create your views here.

def book_listing(request):
    data = {
        'books': Book.objects.order_by('author__last_name', 'title'),
    }

    return render(request, 'book_listing.html', data)