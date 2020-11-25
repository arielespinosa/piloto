from datetime import date
from django import forms
from django.utils.translation import gettext_lazy as _
from trabajador.modelos.trabajo_cientifico import (
    Tesis, Proyecto, Articulo, Servicio, Libro, Resultado
)
from trabajador.modelos.trabajadores import Trabajador, PersonaExterna
from trabajador.modelos.nomencladores import *
from django.db.models import Q
from bootstrap_modal_forms.forms import BSModalForm
from .utils import trabajadores_personas_choices

class DateInput(forms.DateInput):
    input_type = 'date'


class FormProyecto(BSModalForm):
    proyectos = forms.IntegerField()

    class Meta:
        model = Proyecto
        fields = ['centro_costo', 'titulo', 'programa', 'proyectos']


class FormArticulo(BSModalForm):
    proyectos = forms.IntegerField()

    class Meta:
        model = Articulo
        fields = ['proyectos']


class FormLibro(BSModalForm):
    proyectos = forms.IntegerField()

    class Meta:
        model = Libro
        fields = ['proyectos']


class FormResultado(BSModalForm):
    proyectos = forms.IntegerField()

    class Meta:
        model = Resultado
        fields = ['proyectos']


# Forms crear -----------------------------
class FormCrearTesis(BSModalForm):  
    estudiante = forms.ChoiceField(choices=[], required=False) 
    tutores = forms.MultipleChoiceField(choices=[])
    
    class Meta:
        model = Tesis
        exclude = ['content_type', 'object_id']
        widgets = {
            'fecha_inicio': DateInput(),
            'fecha_culminacion': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(FormCrearTesis, self).__init__(*args, **kwargs)
        
        self.fields['estudiante'].choices = trabajadores_personas_choices()
        self.fields['tutores'].choices = trabajadores_personas_choices()

    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data['fecha_inicio']
        if fecha_inicio > date.today():
            raise forms.ValidationError("No pude ser futuro.")
        return fecha_inicio

    def clean(self):
        cleaned_data = super().clean()
        
        estudiante = cleaned_data.get('estudiante')
        tutores = cleaned_data.get('tutores')
        
        if estudiante in tutores:
            self.add_error('estudiante', "El estudiante y el tutor no pueden ser la misma persona.")
            self.add_error('tutores', "El estudiante y el tutor no pueden ser la misma persona.")     
        return cleaned_data


class FormCrearProyecto(BSModalForm):
    jefe = forms.ChoiceField(choices=[])  
    participantes = forms.MultipleChoiceField(choices=[])
    
    class Meta:
        model = Proyecto
        exclude = ['content_type', 'object_id']
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'fecha_inicio': DateInput(),
            'fecha_terminacion': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(FormCrearProyecto, self).__init__(*args, **kwargs)
        
        jefe = Trabajador.objects.all().values_list('pk', 'nombre').union(
            PersonaExterna.objects.all().values_list('pk', 'nombre')
        )

        participantes = Trabajador.objects.all().exclude(pk=self.request.user.trabajador.pk).values_list('pk', 'nombre').union(
            PersonaExterna.objects.all().values_list('pk', 'nombre')
        )

        self.fields['jefe'].choices = list(jefe)
        self.fields['participantes'].choices = list(participantes)


class FormCrearArticulo(BSModalForm):
    autores = forms.MultipleChoiceField(choices=[])

    class Meta:
        model = Articulo
        fields = '__all__'
        labels = {
            'doi':_('DOI'),
            'issn':_('ISSN'),
        }
        widgets = {          
            'fecha_publicado': DateInput(),           
        }

    def __init__(self, *args, **kwargs):
        super(FormCrearArticulo, self).__init__(*args, **kwargs)
        
        autores = Trabajador.objects.all().values_list('pk', 'nombre').union(
            PersonaExterna.objects.all().values_list('pk', 'nombre')
        )

        self.fields['autores'].choices = list(autores)
    
    def clean_fecha_publicado(self):
        fecha = self.cleaned_data['fecha_publicado']
        if fecha > date.today():
            raise forms.ValidationError("No pude ser futuro.")
        return fecha


class FormCrearLibro(BSModalForm):
    autores = forms.MultipleChoiceField(choices=[])

    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {          
            'fecha_publicado': DateInput(),           
        }

    def __init__(self, *args, **kwargs):
        super(FormCrearLibro, self).__init__(*args, **kwargs)
        
        autores = Trabajador.objects.all().values_list('pk', 'nombre').union(
            PersonaExterna.objects.all().values_list('pk', 'nombre')
        )

        self.fields['autores'].choices = list(autores)

    def clean_fecha_publicado(self):
        fecha = self.cleaned_data['fecha_publicado']
        if fecha > date.today():
            raise forms.ValidationError("No pude ser futuro.")
        return fecha


class FormCrearResultado(BSModalForm):
    class Meta:
        model = Resultado
        fields = '__all__'


class FormCrearServicio(BSModalForm):
    responsable = forms.ChoiceField(choices=[])
    participantes = forms.MultipleChoiceField(choices=[])
    
    class Meta:
        model = Servicio
        exclude = ['content_type', 'object_id']
        widgets = {            
            'fecha_inicio': DateInput(),
            'fecha_terminacion': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(FormCrearServicio, self).__init__(*args, **kwargs)
        
        responsable = Trabajador.objects.all().values_list('pk', 'nombre').union(
            PersonaExterna.objects.all().values_list('pk', 'nombre')
        )        
        participantes = Trabajador.objects.all().exclude(pk=self.request.user.trabajador.pk).values_list('pk', 'nombre').union(
            PersonaExterna.objects.all().values_list('pk', 'nombre')
        )

        self.fields['responsable'].choices = list(responsable)
        self.fields['participantes'].choices = list(participantes)

    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data['fecha_inicio']

        if fecha_inicio > date.today():
            raise forms.ValidationError("No pude ser futuro.")
        return fecha_inicio

    def clean_fecha_terminacion(self):
        fecha_terminacion = self.cleaned_data['fecha_terminacion']
     
        if fecha_terminacion < date.today():
            raise forms.ValidationError("No pude ser pasado.")
        return fecha_terminacion

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_terminacion = cleaned_data.get('fecha_terminacion')
        
        """
        if fecha_inicio > fecha_terminacion:
            raise forms.ValidationError("La fecha de iniicio no pude ser mayor a la fecha de terminación.")
        if fecha_terminacion < fecha_inicio:
            raise forms.ValidationError("La fecha de terminación no pude ser menor a la fecha de inicio.")
        """

            




