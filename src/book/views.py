from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from book.models import Book
from . import forms
# Create your views here.

class Home(TemplateView):
    model = Book
    template_name = 'book/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_books'] = Book.objects.order_by('-created')[0:5]
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
