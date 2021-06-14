from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('book/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('create_book/', views.BookCreateView.as_view(), name='create_book'),
    path('update_book/<int:pk>', views.BookUpdateView.as_view(), name='update_book'),
    path('delete_book/<int:pk>', views.BookDeletelView.as_view(), name='delete_book'),
    path('book_genre/', views.BooksByGenreListView.as_view(), name='books_genre'),
    path('book_genre/<int:pk>/', views.BooksByGenreDetailView.as_view(), name='books_by_genre'),
    path('mng/', views.MngTemplateView.as_view(), name='mng')
]
