from datetime import datetime, timedelta
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Avg

from apps.meta.models import MovieView
from apps.movies.models import Movie, Review
from apps.movies.utils import get_client_ip


def movies_view(request):
    search = request.GET.get('search')
    if search:
        movies = Movie.objects.filter(title__icontains=search)
    else:
        movies = Movie.objects.all()
    return render(request, 'movies.html', context={'movies': movies})


def single_movie_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = Review.objects.filter(movie=movie)
    rating = reviews.aggregate(Avg('rating'))
    ip_address = get_client_ip(request)
    movie_view = MovieView.objects.filter(ip=ip_address).last()
    if not movie_view or timezone.now() - movie_view.created_at >= timedelta(hours=1):
        new_view = MovieView.objects.create(movie=movie,
                                ip=ip_address)
        if request.user.is_authenticated:
            new_view.user = request.user
            new_view.save()

    return render(request,
                  'movie.html',
                  context={'movie': movie,
                           'rating': rating['rating__avg'],
                           'ratings':  range(1, 11),
                           'reviews': reviews,
                           'views': movie.views_count})


def add_review_view(request, pk):
    comment = request.POST.get('comment')
    rating = request.POST.get('rating')
    name = request.POST.get('name')
    email = request.POST.get('email')
    movie = Movie.objects.get(id=pk)

    Review.objects.create(comment=comment,
                          rating=rating,
                          name=name,
                          email=email,
                          movie=movie)

    return redirect(reverse('single_movie', kwargs={'pk': pk}))
