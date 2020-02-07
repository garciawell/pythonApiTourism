from django.db import models
from attractions.models import Attractions

class TourismPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    aproved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions)

    def __str__(self):
        return self.name

