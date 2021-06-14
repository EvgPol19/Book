from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from .forms import AuthUserForm

class CustomerLoginView(LoginView):
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    template_name = 'customer/login.html'

    def get_success_url(self):
        return self.success_url