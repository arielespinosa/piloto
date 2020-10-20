from django import forms
from .app_models.elementos import (
    Proyecto, Articulo, Servicio, Libro, LiteraturaGris, Resultado
)
from django.db.models import Q
from bootstrap_modal_forms.forms import BSModalForm


class FormProyecto(BSModalForm):
    proyectos = forms.IntegerField()

    class Meta:
        model = Proyecto
        fields = ['centro_costo', 'nombre', 'programa', 'proyectos']


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


class FormLiteraturaGris(BSModalForm):
    proyectos = forms.IntegerField()

    class Meta:
        model = LiteraturaGris
        fields = ['proyectos']


class FormResultado(BSModalForm):
    proyectos = forms.IntegerField()

    class Meta:
        model = Resultado
        fields = ['proyectos']


class FormServicio(BSModalForm):
    proyectos = forms.IntegerField()

    class Meta:
        model = Servicio
        fields = ['proyectos']


        












