from django.db import models
from apps.common.models import BaseModel
from apps.movies.models import Movie


class MovieView(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} - {self.created_at}"
