from django.forms import ModelForm
from books.models import Review


class BookReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('review',)   