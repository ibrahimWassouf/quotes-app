from django.db import models
from django.urls import reverse

# Create your models here.
class BookQuote(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    quote = models.TextField()

    def __str__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse('quote_detail', args=[str(self.id)])


class Collections(models.Model):
    title = models.CharField(max_length=200)
    quotes = models.ManyToManyField(BookQuote)

    def __str__(self):
        return self.title

