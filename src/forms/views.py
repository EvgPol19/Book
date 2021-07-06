from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models
from . import forms
from django.urls import reverse, reverse_lazy


#----------DETAIL--------------
class SeriesDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.SeriesField
    login_url = '/custumer/login/'
    permission_required = 'forms.view_seriesfield'

class AuthorDetailview(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.AuthorField
    permission_required = 'forms.delete_seriesfield'

class PublisherDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.PublisherField
    permission_required = 'forms.delete_seriesfield'

class GenreDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.GenreField
    permission_required = 'forms.delete_seriesfield'

#----------LIST--------------
class SeriesListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.SeriesField
    permission_required = 'forms.view_seriesfield'

class  AuthorsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.AuthorField
    permission_required = 'forms.delete_seriesfield'

class PublishersListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.PublisherField
    permission_required = 'forms.delete_seriesfield'

class  GenresListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.GenreField
    permission_required = 'forms.delete_seriesfield'

#----------CREATE--------------
class  SeriesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.SeriesField
    form_class = forms.CreateSeriesForm
    permission_required = 'forms.add_seriesfield'

class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.AuthorField
    form_class = forms.CreateAuthorForm
    permission_required = 'forms.delete_seriesfield'

class PublisherCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.PublisherField
    form_class = forms.CreatePublisherForm
    permission_required = 'forms.delete_seriesfield'

class GenreCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.GenreField
    form_class = forms.CreateGenreForm
    permission_required = 'forms.delete_seriesfield'

#----------UPDATE--------------
class  SeriesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.SeriesField
    form_class = forms.CreateSeriesForm
    permission_required = 'forms.change_seriesfield'

class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.AuthorField
    form_class = forms.CreateAuthorForm
    permission_required = 'forms.delete_seriesfield'

class PublisherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.PublisherField
    form_class = forms.CreatePublisherForm
    permission_required = 'forms.delete_seriesfield'

class GenreUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.GenreField
    form_class = forms.CreateGenreForm
    permission_required = 'forms.delete_seriesfield'

#----------DELETE--------------
class SeriesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.SeriesField
    success_url = reverse_lazy('form:mng_forms')
    permission_required = 'forms.delete_seriesfield'

class AuthorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.AuthorField
    success_url = reverse_lazy('form:authors_list')
    permission_required = 'forms.delete_seriesfield'

class PublisherDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.PublisherField
    success_url = reverse_lazy('form:publishers_list')
    permission_required = 'forms.delete_seriesfield'

class GenreDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.GenreField
    success_url = reverse_lazy('form:genres_list')
    permission_required = 'forms.delete_seriesfield'

class MngFormsTemplateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'forms/mng_forms.html'
    permission_required = 'forms.delete_seriesfield'


