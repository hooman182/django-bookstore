from books.models import Book
from django.views.generic import ListView, DetailView

class BookList(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    
class BookDetail(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_details.html'