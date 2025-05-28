from django.contrib import admin
from apps.movies.models import Genre, Actor, Movie, Trailer, Review


admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Trailer)
admin.site.register(Review)
