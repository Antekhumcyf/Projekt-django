from django.db import models
from cities.models import City

class Landmark(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
