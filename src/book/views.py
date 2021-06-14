from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from book.models import Book
from forms.models import GenreField
from . import forms
from forms import models as field


class Home(TemplateView):
    model = Book
    template_name = 'book/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_books'] = Book.objects.order_by('-created')[0:5]
        context['best_books'] = Book.objects.filter(rating__gte = 8).order_by('-created')[0:5]
        context['cheap_books'] = Book.objects.filter(price__lte = 8)[:5]
        return context
class BookDetailView(DetailView):
    model = Book

class BookListView(ListView):
    model = Book

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = forms.CreateBook
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = forms.CreateBook
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class BookDeletelView(PermissionRequiredMixin, DeleteView):
    model = Book
    login_url = '/login/'
    permission_required = 'book_delete_book'
    success_url = reverse_lazy('book:book_list')

class MngTemplateView(TemplateView):
    template_name = 'book/mng.html'

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

