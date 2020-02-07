from django.db import models
from attractions.models import Attractions
from comments.models import Comments
from ratings.models import Rating

class TourismPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    aproved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions)
    comments = models.ManyToManyField(Comments)
    ratings = models.ManyToManyField(Rating)

    def __str__(self):
        return self.name

