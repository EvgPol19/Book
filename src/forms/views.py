from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from . import forms
from django.urls import reverse, reverse_lazy


#----------DETAIL--------------
class SeriesDetailView(DetailView):
    model = models.SeriesField

class AuthorDetailview(DetailView):
    model = models.AuthorField

class PublisherDetailView(DetailView):
    model = models.PublisherField

class GenreDetailView(DetailView):
    model = models.GenreField

#----------LIST--------------
class SeriesListView(ListView):
    model = models.SeriesField

class  AuthorsListView(ListView):
    model = models.AuthorField

class PublishersListView(ListView):
    model = models.PublisherField

class  GenresListView(ListView):
    model = models.GenreField

#----------CREATE--------------
class  SeriesCreateView(CreateView):
    model = models.SeriesField
    form_class = forms.CreateSeriesForm

class AuthorCreateView(CreateView):
    model = models.AuthorField
    form_class = forms.CreateAuthorForm

class PublisherCreateView(CreateView):
    model = models.PublisherField
    form_class = forms.CreatePublisherForm

class GenreCreateView(CreateView):
    model = models.GenreField
    form_class = forms.CreateGenreForm

#----------UPDATE--------------
class  SeriesUpdateView(UpdateView):
    model = models.SeriesField
    form_class = forms.CreateSeriesForm

class AuthorUpdateView(UpdateView):
    model = models.AuthorField
    form_class = forms.CreateAuthorForm

class PublisherUpdateView(UpdateView):
    model = models.PublisherField
    form_class = forms.CreatePublisherForm

class GenreUpdateView(UpdateView):
    model = models.GenreField
    form_class = forms.CreateGenreForm

#----------DELETE--------------
class SeriesDeleteView(DeleteView):
    model = models.SeriesField
    success_url = reverse_lazy('form:mng_forms')

class AuthorDeleteView(DeleteView):
    model = models.AuthorField
    success_url = reverse_lazy('form:authors_list')

class PublisherDeleteView(DeleteView):
    model = models.PublisherField
    success_url = reverse_lazy('form:publishers_list')

class GenreDeleteView(DeleteView):
    model = models.GenreField
    success_url = reverse_lazy('form:genres_list')

class MngFormsTemplateView(TemplateView):
    template_name = 'forms/mng_forms.html'


