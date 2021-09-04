from .models import Experiment
from .models import Modelvariant
from django import forms
from django.db.models.base import Model


class FeedbackForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')
    feedback = forms.CharField(widget=forms.Textarea)
    #id_experiment = forms.IntegerField(label='Experiment ID')
    id_experiment = forms.ModelChoiceField(queryset=Experiment.objects.all())
    variant = forms.ModelChoiceField(queryset=Modelvariant.objects.all())
    #variant = forms.CharField(label='Variant', max_length=2)