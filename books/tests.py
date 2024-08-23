from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from books.models import Book, Review


class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewtest',
            email='reviewtest@gmail.com',
            password='testpass123'
        )
        self.book = Book.objects.create(
            title='grokking algorithms', author='Aditya Y. Bhargava', price=49.99)
        self.review = Review.objects.create(
            book=self.book, review='new review', author=self.user
        )

    def test_book_list(self):
        self.assertEqual(f'{self.book.title}', 'grokking algorithms')
        self.assertEqual(f'{self.book.author}', 'Aditya Y. Bhargava')
        self.assertEqual(f'{self.book.price}', '49.99')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'grokking algorithms')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('books/34533/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'grokking algorithms')
        self.assertContains(response, 'new review')
        self.assertTemplateUsed(response, 'books/book_details.html')
