from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('experiment/<int:experiment_id>', views.experiment_by_id, name='experiment_by_id'),
    path('experiment/model/<int:ifmlmodel_id>', views.ifmlmodel_by_id, name='ifmlmodel_by_id'),
    path('experiment/modeldata/<int:modeldata_id>', views.modeldata_by_id, name='modeldata_by_id'),
    path('ifmlmodel/<int:ifmlmodel_id>', views.ifmlmodel_by_id, name='ifmlmodel_by_id'),
    path('feedback', views.get_feedback, name='get_feedback'),
    path('thankyou', views.thankyou, name='thankyou')
]