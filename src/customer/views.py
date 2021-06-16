from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import forms
from .forms import UserAuthenticationForm


class CustomerLoginView(LoginView):
    form_class = UserAuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'customer/login.html'

    def get_success_url(self):
        return self.success_url

class CustomerLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class ChangePasswordView(PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name = 'customer/pch.html'
class UserCreateView(CreateView):
    model = User
    template_name = 'customer/registration.html'