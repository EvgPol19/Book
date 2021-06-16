from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserAuthenticationForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields=('username', 'password')

class RegistrationUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        # {
        #     'phone', 'country', 'city',
        #     'postcode', 'address_1', 'address_2', 'other'}