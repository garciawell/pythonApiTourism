from django.db import models

class TourismPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    aproved = models.BooleanField(default=False)

    def _str_(self):
        return self.name

