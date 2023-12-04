from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import AddExercise, AddTraining, AddAvaliation,AddHistory, UpdateTraining
import training.models as models
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from django.template.context_processors import csrf
from django import forms


class Home(View):
    template_name = 'home.html'
    t = models.Training.objects.all().values()
    context = {
        'avaliacoes': models.Avaliation.objects.all().values(),
        'treinos': t,
    }
    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(self.context, request))

def avaliation(request):
    avaliation = models.Avaliation.objects.get( id=request.POST.get('avaliation', None) )
    template = loader.get_template('avaliation.html')
    context = {
        'height': avaliation.height,
        'weight': avaliation.weight,
        'fat_count': avaliation.fat_count,
        'date': avaliation.date,
        'id': avaliation.id,
    }
    return HttpResponse(template.render(context))

def training(request):
    training = models.Training.objects.get( id=request.POST.get('training', None) )
    exercises = training.exercises.all().values()
    template = loader.get_template('traininghub.html')
    context = {
        'title': 'Gain Tracker',
        'training': training,
        'trainingName': training.name,
        'workMuscle': 'Posterior',
        'exercises': exercises
    }
    context.update(csrf(request))
    return HttpResponse(template.render(context))

def exercisehistory(request):
    exercise_id = request.POST.get('history', None)
    exercise = get_object_or_404(models.Exercise, id=exercise_id)
    exs = models.ExerciseHistory.objects.filter(exercise_id=exercise)
    series = []
    reps = []
    weights = []
    dates = []
    for ex in exs:
        series.append(ex.nro_series)
        reps.append(ex.nro_reps)
        weights.append(ex.weight)
        dates.append(ex.date)
    template = loader.get_template('exechistory.html')
    context = {
        'name': ex.exercise_id,
        'nro_series': series,
        'nro_reps': reps,
        'weights': weights,
        'dates': dates,
    }
    return HttpResponse(template.render(context))

class UpdateTrainingView(UpdateView):
    model = models.Training
    template_name = 'update.html'
    form_class = UpdateTraining

class UpdateExerciseView(UpdateView):
    model = models.Exercise
    template_name = 'update.html'
    form_class = AddExercise

class UpdateAvaliationView(UpdateView):
    model = models.Avaliation
    template_name = 'update.html'
    form_class = AddAvaliation

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

def save_new_history(request, fk):  # Certifique-se de incluir 'fk' como um parâmetro na função
    if request.method == 'POST':
        form = AddHistory(request.POST)
        if form.is_valid():
            exercise_history = form.save(commit=False)
            exercise = models.Exercise.objects.get(id = fk)
            exercise_history.exercise_id = exercise  # Use o valor 'fk' da URL
            exercise_history.save()
            return redirect('home')  # Redireciona para a URL 'newhistory' após o sucesso
    else:
        form = AddHistory()

    template_name = 'cadastroSimples.html'
    return render(request, template_name, {'form': form})

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


"""
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
    
    
class EditAvaliation(FormView):  
    template_name = 'editbase.html'  # Substitua pelo seu template

    def get(self, request, id):
        objeto = get_object_or_404(models.Avaliation, id=id)
        form = AddAvaliation(instance=objeto)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id):
        objeto = get_object_or_404(models.Avaliation, id=id)
        form = AddAvaliation(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'), id=id)  
        return render(request, self.template_name, {'form': form})
"""
class DeleteTraining(View):

    def deletar_objeto(request, objeto_id):
        objeto = models.Training.objects.get(id=objeto_id)

        return render(request, 'deletar_objeto.html', {'objeto': objeto})
