from django.urls import path
from forms import views as forms

app_name = 'form'
urlpatterns = [
    path('series/', forms.SeriesListView.as_view(), name='series_list'),
    path('authors/', forms.AuthorsListView.as_view(), name='authors_list'),
    path('publishers/', forms.PublishersListView.as_view(), name='publishers_list'),
    path('genres/', forms.GenresListView.as_view(), name='genres_list'),
    path('series/<int:pk>/', forms.SeriesDetailView.as_view(), name='series'),
    path('authors/<int:pk>/', forms.AuthorDetailview.as_view(), name='author'),
    path('publishers/<int:pk>/', forms.PublisherDetailView.as_view(), name='publisher'),
    path('genres/<int:pk>/', forms.GenreDetailView.as_view(), name='genre'),
    path('create_genre/', forms.GenreCreateView.as_view(), name='genre-create'),
    path('update_genre/<int:pk>', forms.GenreUpdateView.as_view(), name='genre-update'),
    path('delete_genre/<int:pk>', forms.GenreDeleteView.as_view(), name='genre-delete'),
    path('create_series/', forms.SeriesCreateView.as_view(), name='series-create'),
    path('update_series/<int:pk>', forms.SeriesUpdateView.as_view(), name='series-update'),
    path('delete_series/<int:pk>', forms.SeriesDeleteView.as_view(), name='series-delete'),
    path('create_publisher/', forms.PublisherCreateView.as_view(), name='publisher-create'),
    path('update_publisher/<int:pk>', forms.PublisherUpdateView.as_view(), name='publisher-update'),
    path('delete_publisher/<int:pk>', forms.PublisherDeleteView.as_view(), name='publisher-delete'),
    path('create_author/', forms.AuthorCreateView.as_view(), name='author-create'),
    path('update_author/<int:pk>', forms.AuthorUpdateView.as_view(), name='author-update'),
    path('delete_author/<int:pk>', forms.AuthorDeleteView.as_view(), name='author-delete'),
    path('mng_forms', forms.MngFormsTemplateView.as_view(), name='mng_forms'),
]