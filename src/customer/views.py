from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from .models import Profile
from .forms import UserCreateForm, ProfileCreateForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import authenticate, login
#----------------login----------------
class UserLoginView(LoginView):
    model = User
    template_name = 'customer/login.html'
    success_url = reverse_lazy('home')
    def get_success_url(self):
        return self.success_url

class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home')

#----------------password----------------
class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'customer/pch.html'
    success_url = reverse_lazy('customer:change_password_done')

class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'customer/pch_done.html'


#----------------registration----------------
class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'customer/user_create.html'
    success_url = reverse_lazy('customer:profile_create')
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
    template_name = 'customer/profile_create.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super().form_valid(form)

#----------------profile----------------
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'customer/profile_detail.html'
    def get_object(self):
        return self.request.user

#----------------update----------------
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'customer/profile_update.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user.customer

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'customer/user_update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user

class ProfileListView(ListView):
    model = Profile
    template_name = 'customer/profiles_list.html'
    paginate_by = 10