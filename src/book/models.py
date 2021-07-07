from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from forms import models as form
from django.urls import reverse
from comments.models import Comment

# Create your models here.
class Book(models.Model):
    books_name = models.CharField(
        verbose_name = 'The title of the book',
        max_length=300
    )
    image = models.ImageField(
        verbose_name='Book image',
        upload_to = 'book/%Y/%m/%d/'
    )
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=6,
        decimal_places=2
    )
    author = models.ManyToManyField(
        form.AuthorField,
        related_name='book_author'
    )
    series = models.ForeignKey(
        form.SeriesField,
        on_delete=models.PROTECT,
        related_name='book_series'
    )
    genre = models.ManyToManyField(
        form.GenreField,
        related_name='book_genre'
    )
    year = models.IntegerField(
        verbose_name = 'Year of publication of the book'
    )
    pages = models.IntegerField(
        verbose_name = 'Number of pages'
    )
    binding = models.CharField(
        verbose_name = 'Book binding',
        max_length=100
    )
    format_book = models.CharField(
        verbose_name = 'Book format',
        max_length=100
    )
    isbn = models.CharField(
        verbose_name = 'ISBN',
        max_length=25
    )
    weight = models.PositiveIntegerField(
        verbose_name='Book weight'
    )
    age = models.CharField(
        verbose_name='Age restrictions',
        max_length=25
    )
    publisher = models.ForeignKey(
        form.PublisherField,
        on_delete=models.PROTECT,
        related_name='book_publisher'
    )
    number_of_books_available = models.IntegerField(
        verbose_name = 'Number of books available'
    )
    is_available = models.BooleanField(
        verbose_name = 'Is the book available?',
        default=False
    )
    rating = models.PositiveIntegerField(
        verbose_name='Rating (0-10)'
    )
    comments = GenericRelation(Comment)
    created = models.DateTimeField(
        verbose_name = 'Was catalogued',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name = 'Was updated',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self) -> str:
        return f'{self.books_name}'

    def get_absolute_url(self):
        return reverse('book:book_detail', args=[self.pk])