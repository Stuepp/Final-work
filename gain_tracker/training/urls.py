from django.urls import path
from . import views

urlpatterns = [
    path('training/', views.training, name='training'),
    path('newexercise/', views.SaveNewExercise.as_view(), name='newexercise'),
    path('newtraining/', views.SaveNewTraining.as_view(), name='newtraining'),
    path('newavaliation/', views.SaveNewAvaliation.as_view(), name='newavaliation'),
]