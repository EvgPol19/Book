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
    path('series/', forms.series_list, name='series_list'),
    path('authors/', forms.authors_list, name='authors_list'),
    path('publishers/', forms.publishers_list, name='publishers_list'),
    path('genres/', forms.genres_list, name='genres_list'),
    path('series/<int:series_id>/', forms.series_detail, name='series'),
    path('authors/<int:authors_id>/', forms.author_detail, name='author'),
    path('publishers/<int:publishers_id>/', forms.publisher_detail, name='publisher'),
    path('genres/<int:genres_id>/', forms.genre_detail, name='genre'),
]
