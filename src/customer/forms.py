from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


# class UserLoginForm(AuthenticationForm, forms.ModelForm):
#     class Meta:
#         model = User
#         fields=('username', 'password')

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password', 'first_name', 'last_name', 'email')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=(
            'phone', 'country', 'city',
            'postcode', 'аddress_1', 'address_2', 'other')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=(
            'phone', 'country', 'city',
            'postcode', 'аddress_1', 'address_2', 'other')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username', 'first_name', 'last_name', 'email')