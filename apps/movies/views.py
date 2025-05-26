from django.shortcuts import render

from apps.movies.models import Movie


def movies_view(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', context={'movies': movies})
