from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE

# Create your models here.

class Modeldata(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created', default=datetime.now)
    model_data = models.FileField(default=None, upload_to='myproject/contex/static/modeldata')
    class Meta:
        verbose_name = 'Model Data'
        verbose_name_plural = 'Model Data'
    def __str__(self):
         return self.title

class Ifmlmodel(models.Model):
    title = models.CharField(default=None, max_length=200)
    create_date = models.DateTimeField('date created', default=datetime.now)
    model = models.FileField(default=None, upload_to='myproject/contex/static/models')
    class Meta:
        verbose_name = 'IFML Model'
        verbose_name_plural = 'IFML Models'
    def __str__(self):
         return self.title

class Modelvariant(models.Model):
    title = models.CharField(default=None, max_length=200)
    create_date = models.DateTimeField('date created', default=datetime.now)
    model = models.FileField(default=None, upload_to='myproject/contex/static/models')
    main_model = models.ForeignKey(Ifmlmodel, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Model Variant'
        verbose_name_plural = 'Model Variants'
    def __str__(self):
         return self.title

class Person(models.Model):
    name = models.CharField(max_length=96)
    email = models.EmailField()
    date_subscribed = models.DateTimeField(default=datetime.now())
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
    def __str__(self):
         return self.name

class Feedback(models.Model):
    content = models.TextField(default=None)
    model_variant = models.CharField(default=None, max_length=2)
    create_date = models.DateTimeField(default=datetime.now())
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

class Experiment(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created', default=datetime.now)
    start_date = models.DateTimeField('date started')
    end_date = models.DateTimeField('date ended')
    hypothesis = models.TextField()
    model = models.ForeignKey(Ifmlmodel, on_delete=models.CASCADE)
    model_data = models.ForeignKey(Modeldata, on_delete=models.CASCADE)
    model_variant = models.ForeignKey(Modelvariant, on_delete=models.CASCADE)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = 'Experiment'
        verbose_name_plural = 'Experiments'
    def __str__(self):
         return self.title