from django import forms
import training.models as models


class AddExercise(forms.ModelForm):
    class Meta:
        model = models.Exercise
        fields = ('name','number_of_series_aimed','number_of_reps_aimed','weight_aimed')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'number_of_series_aimed': forms.NumberInput(attrs={'class': 'form-control', 'required': False, 'min': 1}),
            'number_of_reps_aimed': forms.NumberInput(attrs={'class': 'form-control', 'required': False, 'min': 1}),
            'weight_aimed': forms.NumberInput(attrs={'class': 'form-control', 'required': False,  'min': 0})
        }

class AddTraining(forms.ModelForm):
    class Meta:
        model = models.Training
        fields = ('name', 'exercises')
        widgets = {

        }