from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from . import forms
from django.urls import reverse

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

def genre_create(request):
    if request.method == 'POST':  #обратботка формы
        form = forms.CreateGenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('genres_list'))
        else:
            pass 
    else:
        form = forms.CreateGenreForm()
    ctx = {
        'form': form
    }
    return render(request, template_name='genre_create.html', context=ctx)

def genre_update(request, genres_id):
    if request.method == 'POST':
        obj = models.GenreField.objects.get(pk=genres_id) 
        form = forms.CreateGenreForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('genres_list'))
        else:
            pass 
    else:
        obj = models.GenreField.objects.get(pk=genres_id)
        form = forms.CreateGenreForm(instance=obj)
    ctx = {
        'form': form
    }
    return render(request, template_name='genre_create.html', context=ctx)

def genre_delete(request, genres_id):
    if request.method == 'POST':
        obj = models.GenreField.objects.get(pk=genres_id).delete()
        return HttpResponseRedirect(reverse('genres_list'))
    return render(request, template_name='genre_delete.html')

def series_create(request):
    if request.method == 'POST':  #обратботка формы
        form = forms.CreateSeriesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('series_list'))
        else:
            pass 
    else:
        form = forms.CreateSeriesForm()
    ctx = {
        'form': form
    }
    return render(request, template_name='series_create.html', context=ctx)

def series_update(request, series_id):
    if request.method == 'POST':
        obj = models.SeriesField.objects.get(pk=series_id) 
        form = forms.CreateSeriesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('series_list'))
        else:
            pass 
    else:
        obj = models.SeriesField.objects.get(pk=series_id)
        form = forms.CreateSeriesForm(instance=obj)
    ctx = {
        'form': form
    }
    return render(request, template_name='series_create.html', context=ctx)

def series_delete(request, series_id):
    if request.method == 'POST':
        obj = models.SeriesField.objects.get(pk=series_id).delete()
        return HttpResponseRedirect(reverse('series_list'))
    return render(request, template_name='series_delete.html')

def publisher_create(request):
    if request.method == 'POST':  #обратботка формы
        form = forms.CreatePublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('publishers_list'))
        else:
            pass 
    else:
        form = forms.CreatePublisherForm()
    ctx = {
        'form': form
    }
    return render(request, template_name='publisher_create.html', context=ctx)

def publisher_update(request, publishers_id):
    if request.method == 'POST':
        obj = models.PublisherField.objects.get(pk=publishers_id) 
        form = forms.CreatePublisherForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('publishers_list'))
        else:
            pass 
    else:
        obj = models.PublisherField.objects.get(pk=publishers_id)
        form = forms.CreatePublisherForm(instance=obj)
    ctx = {
        'form': form
    }
    return render(request, template_name='publisher_create.html', context=ctx)

def publisher_delete(request, publishers_id):
    if request.method == 'POST':
        obj = models.PublisherField.objects.get(pk=publishers_id).delete()
        return HttpResponseRedirect(reverse('publishers_list'))
    return render(request, template_name='publisher_delete.html')

def author_create(request):
    if request.method == 'POST':  #обратботка формы
        form = forms.CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authors_list'))
        else:
            pass 
    else:
        form = forms.CreateAuthorForm()
    ctx = {
        'form': form
    }
    return render(request, template_name='publisher_create.html', context=ctx)

def author_update(request, authors_id):
    if request.method == 'POST':
        obj = models.AuthorField.objects.get(pk=authors_id) 
        form = forms.CreateAuthorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authors_list'))
        else:
            pass 
    else:
        obj = models.AuthorField.objects.get(pk=authors_id)
        form = forms.CreateAuthorForm(instance=obj)
    ctx = {
        'form': form
    }
    return render(request, template_name='author_create.html', context=ctx)

def author_delete(request, authors_id):
    if request.method == 'POST':
        obj = models.AuthorField.objects.get(pk=authors_id).delete()
        return HttpResponseRedirect(reverse('pauthors_list'))
    return render(request, template_name='author_delete.html')

