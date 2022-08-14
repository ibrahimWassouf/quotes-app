from django.db import models

# Create your models here.
class BookQuote(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    quote = models.TextField()

    def __str__(self):
        return self.quote