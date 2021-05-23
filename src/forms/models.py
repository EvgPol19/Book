from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class SeriesField(models.Model):
    series = models.CharField(                   #справочник
        verbose_name = 'Books series',
        max_length=30
    )

    def __str__(self) -> str:
        return f'{self.series}'

class GenreField(models.Model):
    genre_name = models.CharField(                   #справочник
        verbose_name = 'Books genre',
        max_length=30
    )
    def __str__(self) -> str:
        return f'{self.genre_name}'

class PublisherField(models.Model):
    publisher = models.CharField(               #справочник
        verbose_name = 'Books publisher',
        max_length=30 
    )
    def __str__(self) -> str:
        return f'{self.publisher}'

class AuthorField(models.Model):
    author = models.CharField(                      #справочник
        verbose_name = 'Author of the book',
        max_length=50
    )
    def __str__(self) -> str:
        return f'{self.author}'    

class Book(models.Model):

    books_name = models.CharField(
        verbose_name = 'The title of the book',
        max_length=150
    )
    author_field = models.ManyToManyField(
        AuthorField
    )
    series_field = models.ForeignKey(
        SeriesField,
        on_delete=models.PROTECT
    )
    genre_field = models.ForeignKey(
        GenreField,
        on_delete=models.PROTECT
    )
    publisher_field = models.ForeignKey(
        PublisherField,
        on_delete=models.PROTECT
    )         
    year = models.IntegerField(
        verbose_name = 'Year of publication of the book'
    )
    number_of_pages = models.IntegerField(
        verbose_name = 'Number of pages'
    )   
    weight_book = models.IntegerField(
        verbose_name = 'Books weight'
    )
    number_of_books_available = models.IntegerField(
        verbose_name = 'Number of books available'
    )
    is_available = models.BooleanField(
        verbose_name = 'Is the book available?',
        default=False
    )
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
        return f'{self.books_name}, {self.year}'       



# Название книги +
# Фото обложки
# Цена (BYN)
# Авторы книги (может содержать несколько авторов) - справочник +
# Серия - справочник +
# Жанры (один или несколько жанров) - справочник +
# Год издания +
# Страниц +
# Переплет
# Формат
# ISBN
# Вес (гр) +
# Возрастные ограничения
# Издательство - справочник +
# Количество книг в наличии +
# Активный (доступен для заказа, Да/Нет) +
# Рейтинг (0 - 10)
# Дата внесения в каталог +
# Дата последнего изменения карточки +