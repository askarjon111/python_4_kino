from django.db import models

from apps.common.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Actor(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born_in = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(BaseModel):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateTimeField()
    duration = models.DurationField()
    poster = models.ImageField(upload_to='movies/poster', blank=True, null=True)

    def __str__(self):
        return self.title


class Trailer(BaseModel):
    title = models.CharField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.movie.title}"
