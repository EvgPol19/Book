from django.contrib import admin
from . import models
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'books_name',
        'price',
        'series',
        'year',
        'pages',
        'binding',
        'format_book',
        'isbn',
        'weight',
        'age',
        'publisher',
        'number_of_books_available',
        'rating',]

admin.site.register(models.Book, BookAdmin)