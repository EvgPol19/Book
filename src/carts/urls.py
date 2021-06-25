from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.CartDetailView.as_view(), name='cart_detail'),
    path('recalculate-cart/', views.RecalculateCart.as_view(), name = 'recalculate-cart'),
]