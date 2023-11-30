from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('training/', views.training, name='training'),
    path('avaliation/', views.avaliation, name='avaliation'),
    path('newexercise/', views.SaveNewExercise.as_view(), name='newexercise'),
    path('newtraining/', views.SaveNewTraining.as_view(), name='newtraining'),
    path('newavaliation/', views.SaveNewAvaliation.as_view(), name='newavaliation'),
    path('newhistory/', views.SaveNewHistory.as_view(), name='newhistory'),
    path('edittraining/<int:id>/', views.EditTraining.as_view(), name='edittraining'),
    path('editexercise/<int:id>/', views.EditExercise.as_view(), name='editexercise'),
    path('editavaliation/<int:id>/', views.EditAvaliation.as_view(), name='editavaliation'),

]