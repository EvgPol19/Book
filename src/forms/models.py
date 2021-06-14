from django.db import models
from django.db.models.fields import TextField
from django.urls import reverse

# Create your models here.
class SeriesField(models.Model):
    series = models.CharField(                   #справочник
        verbose_name = 'Books series',
        max_length=30
    )

    def __str__(self) -> str:
        return f'{self.series}'

    def get_absolute_url(self):
        return reverse('form:series', args=[self.pk])

class GenreField(models.Model):
    genre_name = models.CharField(                   #справочник
        verbose_name = 'Books genre',
        max_length=30
    )
    genre_descrption = models.TextField(
        verbose_name = 'Genre description',
        blank=True, #оба значения, разрешвют полю быть пустым!!!
        null=True
    )
    def __str__(self) -> str:
        return f'{self.genre_name}'

    def get_absolute_url(self):
        return reverse('form:genre', args=[self.pk])

class PublisherField(models.Model):
    publisher = models.CharField(               #справочник
        verbose_name = 'Books publisher',
        max_length=30
    )
    def __str__(self) -> str:
        return f'{self.publisher}'

    def get_absolute_url(self):
        return reverse('form:publisher', args=[self.pk])

class AuthorField(models.Model):
    author = models.CharField(                      #справочник
        verbose_name = 'Author of the book',
        max_length=50
    )
    author_descrption = models.TextField(
        verbose_name = 'Author description',
        blank=True, #оба значения, разрешвют полю быть пустым!!!
        null=True
    )
    def __str__(self) -> str:
        return f'{self.author}'

    def get_absolute_url(self):
        return reverse('form:author', args=[self.pk])