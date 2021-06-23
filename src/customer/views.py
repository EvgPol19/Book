from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import UserAuthenticationForm, UserCreateForm, UserUpdateForm


#----------------login----------------
class UserLoginView(LoginView):
    form_class = UserAuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'customer/login.html'

    def get_success_url(self):
        return self.success_url

class CustomerLogoutView(LogoutView):
    success_url = reverse_lazy('home')

#----------------registration----------------
class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'customer/registration.html'
    success_url = reverse_lazy('customer:user_update')

class UserUpdateView(UpdateView):
    model = Profile
    form_class = UserUpdateForm
    template_name = 'customer/user_update.html'
    success_url = reverse_lazy('home')


#----------------password----------------
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'customer/pch.html'
# class UserCreateView(CreateView):
#     model = UserProfile
#     template_name = 'customer/registration.html'
#     form_class = RegistrationUserForm