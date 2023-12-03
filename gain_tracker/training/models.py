from django.db import models
from django import forms
from django.urls import reverse_lazy

class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number_of_series_aimed = models.IntegerField()
    number_of_reps_aimed = models.IntegerField()
    weight_aimed = models.FloatField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('home')

class Training(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    exercises = models.ManyToManyField(Exercise)

    def get_absolute_url(self):
        return reverse_lazy('home')

class Avaliation(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.FloatField()
    weight = models.FloatField()
    fat_count = models.FloatField()
    date = models.DateField()

    def get_absolute_url(self):
        return reverse_lazy('home')

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    phone = models.IntegerField()
    email = models.TextField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

class ExerciseHistory(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    nro_series = models.IntegerField()
    nro_reps = models.IntegerField()
    exercise_id = models.ForeignKey(Exercise,on_delete=models.CASCADE)
    weight = models.FloatField()