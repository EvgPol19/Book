from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('login/', views.CustomerLoginView.as_view(), name='login'),
    path('registration/', views.UserCreateView.as_view(), name='registration'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
]
