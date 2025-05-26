from django.urls import path

from apps.movies.views import movies_view, single_movie_view


urlpatterns = [
    path('', movies_view, name='movies_list'),
    path('watch/<int:pk>', single_movie_view, name='single_movie'),
]

