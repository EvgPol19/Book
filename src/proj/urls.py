"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from forms import views as forms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('series/', forms.SeriesListView.as_view(), name='series_list'),
    path('authors/', forms.AuthorsListView.as_view(), name='authors_list'),
    path('publishers/', forms.PublishersListView.as_view(), name='publishers_list'),
    path('genres/', forms.GenresListView.as_view(), name='genres_list'),
    path('series/<int:pk>/', forms.SeriesDetailView.as_view(), name='series'),
    path('authors/<int:pk>/', forms.AuthorDetailview.as_view(), name='author'),
    path('publishers/<int:pk>/', forms.PublisherDetailView.as_view(), name='publisher'),
    path('genres/<int:pk>/', forms.GenreDetailView.as_view(), name='genre'),
    path('create-genre/', forms.GenreCreateView.as_view(), name='genre-create'),
    path('update-genre/<int:pk>', forms.GenreUpdateView.as_view(), name='genre-update'),
    path('delete-genre/<int:pk>', forms.GenreDeleteView.as_view(), name='genre-delete'),
    path('create-series/', forms.SeriesCreateView.as_view(), name='series-create'),
    path('update-series/<int:pk>', forms.SeriesUpdateView.as_view(), name='series-update'),
    path('delete-series/<int:pk>', forms.SeriesDeleteView.as_view(), name='series-delete'),
    path('create-publisher/', forms.PublisherCreateView.as_view(), name='publisher-create'),
    path('update-publisher/<int:pk>', forms.PublisherUpdateView.as_view(), name='publisher-update'),
    path('delete-publisher/<int:pk>', forms.PublisherDeleteView.as_view(), name='publisher-delete'),
    path('create-author/', forms.AuthorCreateView.as_view(), name='author-create'),
    path('update-author/<int:pk>', forms.AuthorUpdateView.as_view(), name='author-update'),
    path('delete-author/<int:pk>', forms.AuthorDeleteView.as_view(), name='author-delete'),
    path('', forms.Home.as_view(), name='home')
]
