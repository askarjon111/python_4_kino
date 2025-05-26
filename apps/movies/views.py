from django.shortcuts import render, get_object_or_404

from apps.movies.models import Movie


def movies_view(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', context={'movies': movies})


def single_movie_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie.html', context={'movie': movie})
