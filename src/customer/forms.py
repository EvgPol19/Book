from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class UserAuthenticationForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields=('username', 'password')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # {
        #     'phone', 'country', 'city',
        #     'postcode', 'address_1', 'address_2', 'other'}


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )