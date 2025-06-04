from django.db import models
from django.contrib.auth.models import User
from apps.common.models import BaseModel
from apps.movies.models import Movie


class MovieView(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    ip = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.movie} - {self.created_at}"
