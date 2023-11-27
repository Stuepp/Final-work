from django.urls import path
from . import views

urlpatterns = [
    path('training/', views.training, name='training'),
    path('training/newexercise', views.SaveNewExercise.as_view(), name='newexercise'),
]