from django.contrib import admin
from django.urls import path
from appatencion.views import PacienteView
from django.conf import settings
app_name = "appatencion"
urlpatterns = [
    path('paciente/', PacienteView.as_view(), name='paciente'),
]
