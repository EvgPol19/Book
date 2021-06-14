from django import forms
from . import models

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.GenreField
        fields = '__all__'

class CreateSeriesForm(forms.ModelForm):
    class Meta:
        model = models.SeriesField
        fields = '__all__'

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.PublisherField
        fields = '__all__'

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.AuthorField
        fields = '__all__'


