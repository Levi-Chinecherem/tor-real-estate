# urls.py in the Surveyors app

from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.surveyor_application, name='surveyor_application'),
    path('survey/<int:land_id>/', views.survey_land, name='survey_land'),
    path('not-approved/', views.not_approved, name='not_approved'),
]
