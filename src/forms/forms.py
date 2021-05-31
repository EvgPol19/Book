from django import forms
from . import models

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.GenreField
        fields = {
            'genre_name',
            'genre_descrption',
        }

class CreateSeriesForm(forms.ModelForm):
    class Meta:
        model = models.SeriesField
        fields = {
            'series',
        }

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.PublisherField
        fields = {
            'publisher',
        }

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.AuthorField
        fields = {
            'author',
            'author_descrption',
        }


