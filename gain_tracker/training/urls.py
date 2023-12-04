from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('training/', views.training, name='training'),
    path('avaliation/', views.avaliation, name='avaliation'),
    path('training/history/', views.exercisehistory, name='history'),
    path('newexercise/', views.SaveNewExercise.as_view(), name='newexercise'),
    path('newtraining/', views.SaveNewTraining.as_view(), name='newtraining'),
    path('newavaliation/', views.SaveNewAvaliation.as_view(), name='newavaliation'),
    path('training/newhistory/<int:fk>/', views.save_new_history, name='newhistory'),
    path('training/update/<int:pk>/', views.UpdateTrainingView.as_view(), name='updatetraining'),
    path('training/updateexercise/<int:pk>/', views.UpdateExerciseView.as_view(), name='updateexercise'),
    path('avaliation/updateavaliation/<int:pk>/', views.UpdateAvaliationView.as_view(), name='updateavaliation'),
]