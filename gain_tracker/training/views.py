from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import AddExercise, AddTraining, AddAvaliation,AddHistory
import training.models as models
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy


def home(request):
    template = loader.get_template('home.html')
    context = {

    }
    return HttpResponse(template.render(context))

def avaliation(request):
    template = loader.get_template('avaliation.html')
    context = {

    }
    return HttpResponse(template.render(context))

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
    success_url = reverse_lazy('newexercise')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_date(self, **kwargs):
        context = super(SaveNewExercise, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Gain Tracker'
        context['title'] = 'Gain Tracker'
        return context

class SaveNewTraining(FormView):
    template_name = 'cadastroSimples.html'
    form_class = AddTraining
    success_url = reverse_lazy('newtraining')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class SaveNewAvaliation(FormView):
    template_name = 'cadastroSimples.html'
    form_class = AddAvaliation
    success_url = reverse_lazy('newavaliation')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class SaveNewHistory(FormView):
    template_name = 'cadastroSimples.html'
    form_class = AddHistory
    success_url = reverse_lazy('newavaliation')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class EditTraining(FormView):  
    template_name = 'editbase.html'  # Substitua pelo seu template

    def get(self, request, id):
        objeto = get_object_or_404(models.Training, id=id)
        form = AddTraining(instance=objeto)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id):
        objeto = get_object_or_404(models.Training, id=id)
        form = AddTraining(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'), id=id)  
        return render(request, self.template_name, {'form': form})
    
class EditExercise(FormView):  
    template_name = 'editbase.html'  # Substitua pelo seu template

    def get(self, request, id):
        objeto = get_object_or_404(models.Exercise, id=id)
        form = AddExercise(instance=objeto)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id):
        objeto = get_object_or_404(models.Exercise, id=id)
        form = AddExercise(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'), id=id)  
        return render(request, self.template_name, {'form': form})
    