# cities/models.py
from django.db import models

class City(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
