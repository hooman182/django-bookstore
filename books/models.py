from django.db import models
from django.urls import reverse
import uuid


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    