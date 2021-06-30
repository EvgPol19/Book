from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.CartDetailView.as_view(), name='cart_detail'),
    path('delete_book_in_cart/<int:pk>/', views.BookInCartDeleteView.as_view(), name='delete_book_in_cart'),
    path('cart_update/', views.CartView.as_view(), name='cart_update'),
]