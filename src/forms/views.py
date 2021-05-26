from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def series_detail(request, series_id):
    series_detail = models.SeriesField.objects.get(pk=series_id)
    ctx = {
        'series_detail': series_detail
    }
    return render(request, template_name='series_detail.html', context=ctx) 

def author_detail(request, authors_id):
    author_detail = models.AuthorField.objects.get(pk=authors_id)
    ctx = {
        'author_detail': author_detail
    }
    return render(request, template_name='author_detail.html', context=ctx)

def publisher_detail(request, publishers_id):
    publisher_detail = models.PublisherField.objects.get(pk=publishers_id)
    ctx = {
        'publisher_detail': publisher_detail
    }
    return render(request, template_name='publisher_detail.html', context=ctx) 

def genre_detail(request, genres_id):
    genre_detail = models.GenreField.objects.get(pk=genres_id)
    ctx = {
        'genre_detail': genre_detail
    }
    return render(request, template_name='genre_detail.html', context=ctx) 

def series_list(request):
    series_list = models.SeriesField.objects.all()
    ctx = {
        'series_list': series_list
    }
    return render(request, template_name='series_list.html', context=ctx)

def authors_list(request):
    authors_list = models.AuthorField.objects.all()
    ctx = {
        'authors_list': authors_list
    }
    return render(request, template_name='authors_list.html', context=ctx)

def publishers_list(request):
    publishers_list = models.PublisherField.objects.all()
    ctx = {
        'publishers_list': publishers_list
    }
    return render(request, template_name='publishers_list.html', context=ctx)

def genres_list(request):
    genres_list = models.GenreField.objects.all()
    ctx = {
        'genres_list': genres_list
    }
    return render(request, template_name='genres_list.html', context=ctx)
