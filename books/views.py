from django.shortcuts import redirect
from books.forms import BookReviewForm
from books.models import Book
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q


class BookList(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"


class BookDetail(LoginRequiredMixin, PermissionRequiredMixin, FormMixin, DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_details.html"
    form_class = BookReviewForm
    login_url = "account_login"
    permission_required = "books.special_status"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        book = self.get_object()
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.book = book
            review.save()

        return redirect(book.get_absolute_url())


class SearchResultView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
