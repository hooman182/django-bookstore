from django.shortcuts import redirect
from books.forms import BookReviewForm
from books.models import Book
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

class BookList(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    
class BookDetail(FormMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_details.html'
    form_class = BookReviewForm
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        book = self.get_object()
        if form.is_valid(): 
            review = form.save(commit=False)
            review.author = request.user
            review.book = book
            review.save()
            
        return redirect(book.get_absolute_url())