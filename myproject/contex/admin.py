from django.contrib import admin
from django.db.models.base import Model

admin.site.site_header = "ContEx Admin"
admin.site.index_title = "Welcome to ContEx"
admin.site.site_title = "ContEx"

# Register your models here.
from .models import Experiment
admin.site.register(Experiment)

from .models import Modeldata
admin.site.register(Modeldata)

from .models import Ifmlmodel
admin.site.register(Ifmlmodel)

from .models import Modelvariant
admin.site.register(Modelvariant)

from .models import Feedback
admin.site.register(Feedback)

from .models import Person
admin.site.register(Person)