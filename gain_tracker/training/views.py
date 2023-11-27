from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import AddExercise
import training.models as models
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy

def training(request):
    template = loader.get_template('traininghub.html')
    # get training
    #training = models.Training.first()
    context = {
        'title': 'Gain Tracker',
        'trainingName': 'Leg',
        'cardTextContent': 'O agachamento é um exercício físico de força em que o praticante abaixa os quadris a partir de uma posição em pé e depois se levanta.',
        'cardSecondaryTextContent': 'Something',
        'workMuscle': 'Posterior',
        'exerciseName': 'Agachamento',
    }
    return HttpResponse(template.render(context))


class SaveNewExercise(FormView):
    template_name = 'cadastroSimples.html'
    form_class = AddExercise
    succes_url = reverse_lazy('newexercise')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_date(self, **kwargs):
        context = super(SaveNewExercise, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Gain Tracker'
        context['title'] = 'Gain Tracker'
        return context
