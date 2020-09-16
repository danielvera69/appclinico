from .models import Horario, Paciente
from django import forms


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ('dia', 'desde', 'hasta', 'estado')
        label = {
            'dia': 'Dia Semana',
            'desde': 'Hora Desde',
            'hasta': 'Hora Hasta',
            'estado': 'Estado'
        }
        widgets = {
            'dia': forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Dia de la Semana'
                }
            ),
            'desde': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'hh:mm'
                }
            ),
            'hasta': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'hh:mm'
                }
            ),

            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"

        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'sangre': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hijos': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
