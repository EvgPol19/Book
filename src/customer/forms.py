from django import forms
from django.db.models import fields
from customer import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields=('username', 'password')