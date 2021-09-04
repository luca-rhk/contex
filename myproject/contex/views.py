from contex.forms import FeedbackForm
from django.db.models.base import Model
from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from .models import Experiment
from .models import Ifmlmodel
from .models import Modeldata
from .models import Feedback
from .models import Person

def index(request):
    #return HttpResponse("Hello, world!")
    return render(request, 'index.html')

def experiment_by_id(request, experiment_id):
    experiment = Experiment.objects.get(pk=experiment_id)
    #model = experiment.model.url
    return render(request, 'experiment_details.html', {'experiment':experiment})

def ifmlmodel_by_id(request, ifmlmodel_id):
    ifmlmodel = Ifmlmodel.objects.get(pk=ifmlmodel_id)
    return render(request, 'model_details.html', {'ifmlmodel':ifmlmodel})

def modeldata_by_id(request, modeldata_id):
    modeldata = Modeldata.objects.get(pk=modeldata_id)
    return render(request, 'modeldata_details.html', {'modeldata':modeldata})

def get_feedback(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            experiment = form.cleaned_data['id_experiment']
            variant = form.cleaned_data['variant']
            p = Person(name=name, email=email, date_subscribed=datetime.now())
            f = Feedback(content=feedback, experiment=experiment, model_variant=variant, create_date=datetime.now())
            p.save()
            f.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thankyou')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})

def thankyou(request):
    return render(request, 'thankyou.html')