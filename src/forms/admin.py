from django.contrib import admin
from . import models
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'created',
        'updated',
        'books_name',
        'year']
class SeriesFielddAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'series']

class GenreFieldAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'genre_name',
        'genre_descrption']

class PublisherFieldAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'publisher']

class AuthorFieldAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'author',
        'author_descrption']
admin.site.register(models.AuthorField, AuthorFieldAdmin)
admin.site.register(models.PublisherField, PublisherFieldAdmin)
admin.site.register(models.GenreField, GenreFieldAdmin)
admin.site.register(models.SeriesField, SeriesFielddAdmin)
# admin.site.register(models.Book,BookAdmin)