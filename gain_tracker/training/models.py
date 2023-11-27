from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    number_of_series_aimed = models.IntegerField()
    number_of_reps_aimed = models.IntegerField()
    weight_aimed = models.FloatField()

class Training(models.Model):
    name = models.CharField(max_length=255)
    exercises = models.ManyToManyField(Exercise)