from django import forms
from .models import Order


class OrderCreateForm(forms.Form):
    country = forms.CharField(label='country', required=True, widget=forms.TextInput, help_text='Enter country')
    city = forms.CharField(label='city', required=True, widget=forms.TextInput, help_text='Enter city')
    address = forms.CharField(label='address', required=True, widget=forms.TextInput, help_text='Enter address')
    phone = forms.CharField(label='phone', required=True, widget=forms.TextInput, help_text='Enter phone number (+3752911122333)')
    other = forms.CharField(label='other information', required=True, widget=forms.TextInput, help_text='Enter other information')
    status = forms.CharField(label='status', required=True, widget=forms.TextInput, help_text='Choise status order')

