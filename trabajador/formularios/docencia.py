from django.db.models import CharField, Value as V
from django.db.models.functions import Concat
import datetime
from CFA import settings
from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from trabajador.modelos.trabajo_cientifico import (Tesis, Articulo, Resultado, Proyecto)
from trabajador.modelos.docencia import *


class DateInput(forms.DateInput):
    input_type = 'date'


class FormCrearCentroEstudios(BSModalForm):  
    class Meta:
        model = CentroEstudios
        fields = ['nombre', 'pais']


class FormEventos(forms.Form):
    eventos = forms.ModelMultipleChoiceField(label='Eventos en los que no ha participado', queryset=None, required=False)
    class Meta:
        fields = ['eventos']


class FormCertificaciones(forms.Form):
    certificaciones = forms.ModelMultipleChoiceField(label='Certificaciones que no posee', queryset=None, required=False)
    class Meta:
        fields = ['certificaciones']


class FormOponencias(forms.Form):
    oponencias = forms.ModelMultipleChoiceField(label='Oponencias en las que no ha participado', queryset=None, required=False)
    class Meta:
        fields = ['oponencias']


class FormTribunales(forms.Form):
    tribunales = forms.ModelMultipleChoiceField(label='Tribunales en los que no ha participado', queryset=None, required=False)
    class Meta:
        fields = ['tribunales']


class FormPonencias(forms.Form):
    ponencias = forms.ModelMultipleChoiceField(label='Ponencias en las que no ha participado', queryset=None, required=False)
    class Meta:
        fields = ['ponencias']


class FormCrearEvento(BSModalForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'lugar', 'nivel', 'descripcion']
        help_texts = {
            'nombre': 'El nombre es sensible a las mayúsculas',
        }
        error_messages = {
            'nombre': {
                'max_length': "This writer's name is too long.",
            },
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'fecha': DateInput(),
        }
    
    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False


class FormCrearOponencia(BSModalForm):  
    oponentes = forms.MultipleChoiceField(choices=[], required=False)
    elemento = forms.ChoiceField(choices=[])

    class Meta:
        model = Oponencia
        fields = ['oponentes', 'fecha', 'elemento']
        widgets = {
            'fecha': DateInput(),
        }

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False

    def __init__(self, *args, **kwargs):
        super(FormCrearOponencia, self).__init__(*args, **kwargs)
        
        choices = [(t.pk, '{0} {1} {2}'.format(t.nombre, t.apellido1, t.apellido2)) for t in Trabajador.objects.all().exclude(pk=self.request.user.trabajador.pk) ]       
        choices += [(p.pk, '{0} {1} {2}'.format(p.nombre, p.apellido1, p.apellido2)) for p in PersonaExterna.objects.all()]
   
        elemento = Articulo.objects.all().values_list('pk', 'titulo').union(
            Tesis.objects.all().values_list('pk', 'titulo'),
            Resultado.objects.all().values_list('pk', 'titulo'),
            Proyecto.objects.all().values_list('pk', 'titulo')
        )

        self.fields['oponentes'].choices = choices
        self.fields['elemento'].choices = list(elemento)


class FormCrearPonencia(BSModalForm):  
    autores = forms.MultipleChoiceField(choices=[], required=False)
    
    class Meta:
        model = Ponencia
        fields = '__all__'

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False


    def __init__(self, *args, **kwargs):
        super(FormCrearPonencia, self).__init__(*args, **kwargs)
        
        autores = Trabajador.objects.all().exclude(pk=self.request.user.trabajador.pk).values_list('pk', 'nombre').union(
            PersonaExterna.objects.all().values_list('pk', 'nombre')
        )

        self.fields['autores'].choices = list(autores)


class FormCrearPonenciaRealizada(BSModalForm):  
    class Meta:
        model = PonenciasRealizadas
        exclude = ['ponencia', 'ponente']

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False


class FormCrearTribunal(BSModalForm):
    miembros = forms.MultipleChoiceField(choices=[],required=False)
    
    class Meta:
        model = Tribunal
        fields = '__all__'
        widgets = {
            'fecha': DateInput(),
            #'tesis': forms.Select(attrs={'size': 13})
        }

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False
    
    def __init__(self, *args, **kwargs):
        super(FormCrearTribunal, self).__init__(*args, **kwargs)
        
        miembros = Trabajador.objects.all().exclude(pk=self.request.user.trabajador.pk).values_list('pk', 'nombre').union(
            PersonaExterna.objects.all().values_list('pk', 'nombre')
        )

        self.fields['miembros'].choices = list(miembros)


class FormCrearComision(BSModalForm):
    integrantes = forms.MultipleChoiceField(choices=[])

    class Meta:
        model = Comision
        fields = '__all__'
        widgets = {
            'fecha': DateInput(),
        }

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False
    
    def __init__(self, *args, **kwargs):
        super(FormCrearComision, self).__init__(*args, **kwargs)
        
        integrantes = Trabajador.objects.all().values_list('pk', 'nombre').union(
            PersonaExterna.objects.all().values_list('pk', 'nombre')
        )

        self.fields['integrantes'].choices = list(mieintegrantesmbros)


class FormCrearTutoria(BSModalForm):

    class Meta:
        model = Tutoria
        exclude = ['tutor']
        widgets = {
            'fecha_inicio': DateInput(),
        }




