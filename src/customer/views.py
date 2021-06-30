from django.shortcuts import render, redirect
from django.contrib.auth import views as lgps_view
from django.views.generic import CreateView, UpdateView, DetailView, ListView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import UserCreateForm, ProfileCreateForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import authenticate, login
#----------------login----------------
class UserLoginView(lgps_view.LoginView):
    model = User
    template_name = 'customer/login.html'
    success_url = reverse_lazy('home')
    def get_success_url(self):
        return self.success_url

class UserLogoutView(lgps_view.LogoutView):
    next_page = reverse_lazy('home')

#----------------password----------------
class UserPasswordChangeView(lgps_view.PasswordChangeView):
    template_name = 'customer/pch.html'
    success_url = reverse_lazy('customer:change_password_done')

class UserPasswordChangeDoneView(lgps_view.PasswordChangeDoneView):
    template_name = 'customer/pch_done.html'


#----------------registration----------------
class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'customer/registration.html'
    success_url = reverse_lazy('customer:user_update')
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        aut_user.groups.add(Group.objects.get(name='Customers'))
        login(self.request, aut_user)
        return form_valid

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'customer/user_update.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super().form_valid(form)

#----------------profile----------------
class UserProfileDetailView(DetailView):
    model = User
    template_name = 'customer/profile_detail.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_data'] = Profile.objects.filter(user = self.request.user)
        return context

#----------------update profile----------------
class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'customer/profile_update.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('home')

class UserUpdateView(UpdateView):
    model = User
    template_name = 'customer/user_update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')

