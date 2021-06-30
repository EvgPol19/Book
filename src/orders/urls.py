from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('create_order/', views.OrderCreate.as_view(), name='create_order'),
    path('thanks/', views.Thanks.as_view(), name='thanks'),
]