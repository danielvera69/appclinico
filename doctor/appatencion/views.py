from django.shortcuts import render
from django.views.generic.base import TemplateView


class InicioView(TemplateView):
    template_name = "index.html"


class PacienteView(TemplateView):
    template_name = "atencion/paciente/paciente.html"
