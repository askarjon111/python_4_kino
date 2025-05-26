from django.urls import path

from apps.movies.views import movies_view


urlpatterns = [
    path('', movies_view, name='movies_list')
]

