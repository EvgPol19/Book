from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from book.models import Book
from forms.models import GenreField, AuthorField, SeriesField, PublisherField
from . import forms
from forms import models as field
from django.db.models import Q


class Home(TemplateView):
    model = Book
    template_name = 'book/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_books'] = Book.objects.order_by('-created')[:5]
        context['best_books'] = Book.objects.filter(rating__gte = 8).order_by('-created')[:5]
        context['cheap_books'] = Book.objects.filter(price__lte = 8).order_by('-created')[:5]
        return context
class BookDetailView(DetailView):
    model = Book

class BookListView(ListView):
    model = Book
#____________search_______________
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(books_name__icontains=q))
        return qs
    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q')
        return super().get_context_data(**kwargs)

class BookCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Book
    form_class = forms.CreateBook
    login_url = '/custumer/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'book.add_book'
    success_url = reverse_lazy('book:book_list')

class BookUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Book
    form_class = forms.CreateBook
    login_url = '/custumer/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'book.change_book'
    success_url = reverse_lazy('book:book_list')

class BookDeletelView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Book
    login_url = '/login/'
    permission_required = 'book.delete_book'
    success_url = reverse_lazy('book:book_list')

class MngTemplateView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'book/mng.html'
    permission_required = 'book.delete_book'

#------------------by genre------------------
class BooksByGenreListView(ListView):
    model = GenreField
    template_name = 'book/books_by_genre.html'
class BooksByGenreDetailView(DetailView):
    model = GenreField
    template_name = 'book/books_by_genre_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_books'] = Book.objects.filter(genre = self.object.pk)
        return context

#------------------by author------------------
class BooksByAuthorListView(ListView):
    model = AuthorField
    template_name = 'book/books_by_author.html'
class BooksByAuthorDetailView(DetailView):
    model = AuthorField
    template_name = 'book/books_by_author_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_books'] = Book.objects.filter(author = self.object.pk)
        return context

#------------------by series------------------
class BooksBySeriesListView(ListView):
    model = SeriesField
    template_name = 'book/books_by_series.html'

class BooksBySeriesDetailView(DetailView):
    model = SeriesField
    template_name = 'book/books_by_series_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['series_books'] = Book.objects.filter(series = self.object.pk)
        return context


#------------------by publisher------------------
class BooksByPublisherListView(ListView):
    model = PublisherField
    template_name = 'book/books_by_publisher.html'

class BooksByPublisherDetailView(DetailView):
    model = PublisherField
    template_name = 'book/books_by_publisher_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publisher_books'] = Book.objects.filter(publisher = self.object.pk)
        return context


