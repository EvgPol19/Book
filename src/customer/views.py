from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView, TemplateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserCreateView(CreateView):
    model = Profile
    form_class = UserCreationForm
    template_name = 'customer/registration.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




# class CustomerLoginView(LoginView):
#     form_class = UserAuthenticationForm
#     success_url = reverse_lazy('home')
#     template_name = 'customer/login.html'

#     def get_success_url(self):
#         return self.success_url

# class CustomerLogoutView(LogoutView):
#     success_url = reverse_lazy('home')

# class ChangePasswordView(PasswordChangeView):
#     form_class = forms.PasswordChangeForm
#     template_name = 'customer/pch.html'
# class UserCreateView(CreateView):
#     model = UserProfile
#     template_name = 'customer/registration.html'
#     form_class = RegistrationUserForm