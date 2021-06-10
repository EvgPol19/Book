from django import forms
from . import models

class CreateBook(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
