from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from ratings.models import Rating


class Movie(models.Model):
    title = models.CharField(max_length=120)
    overview = models.TextField()
    poster = models.ImageField(upload_to="media/")
    release_date = models.DateField(
        blank=True,
        null=True,
        auto_now=False,
        auto_now_add=False,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    ratings = GenericRelation(Rating)  # queryset
