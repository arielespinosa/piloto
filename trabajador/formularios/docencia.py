from django.db.models import CharField, Value as V
from django.db.models.functions import Concat
import datetime
from CFA import settings
from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from trabajador.modelos.trabajo_cientifico import (Tesis, Articulo, Resultado, Proyecto)
from trabajador.modelos.docencia import *
from .utils import trabajadores_personas_choices, cursos_choices


class DateInput(forms.DateInput):
    input_type = 'date'


class FormSeleccionarCursos(forms.Form):
    cursos = forms.MultipleChoiceField(label='Cursos en los que no ha participado', choices=[], required=False) 
    
    class Meta:
        fields = ['cursos']

    def __init__(self, trabajador=None, *args, **kwargs):
        super(FormSeleccionarCursos, self).__init__(*args, **kwargs)
        self.fields['cursos'].choices = cursos_choices(trabajador)


class FormCrearCentroEstudios(BSModalForm):  
    class Meta:
        model = CentroEstudios
        fields = ['nombre', 'pais']


class FormEventos(forms.Form):
    eventos = forms.ModelMultipleChoiceField(label='Eventos en los que no ha participado', queryset=None, required=False)
    class Meta:
        fields = ['eventos']


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


class FormCrearCertificarTrabajador(BSModalForm):  
    
    class Meta:
        model = CertificarTrabajador
        exclude = ['trabajador']
        widgets = {
            'fecha': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(FormCrearCertificarTrabajador, self).__init__(*args, **kwargs)

        # Certificaciones que el trabajador no tenga 
        # ni por curso ni asociada directamente
        #self.fields['certificacion'].queryset = trabajadores_personas_choices()


class FormCrearCurso(BSModalForm): 

    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'centro_estudios':forms.Select(attrs={'id': 'id_centro_estudios'}),
        }


class FormCrearCursoRealizado(BSModalForm):  
    profesor = forms.ChoiceField(choices=[])
    estudiantes = forms.MultipleChoiceField(choices=[])

    class Meta:
        model = CursoRealizado
        fields = [
            'fecha_inicio', 
            'fecha_terminacion', 
            'curso',
            'estudiantes', 
        ]
        widgets = {
            'fecha_terminacion': DateInput(),
            'fecha_inicio': DateInput(),
        }
    
    @property
    def is_empity(self):
        self.is_valid()
        #print(self.clean())
        #print(self.fields.keys())
        return False

    def __init__(self, *args, **kwargs):
        super(FormCrearCursoRealizado, self).__init__(*args, **kwargs)
        self.fields['profesor'].choices = trabajadores_personas_choices()
        self.fields['estudiantes'].choices = trabajadores_personas_choices()

    def clean(self):
        cleaned_data = super().clean()
        profesor = cleaned_data.get('profesor')
        estudiantes = cleaned_data.get('estudiantes')

        print(estudiantes)
        print(profesor)
        print("hola")
        
        if profesor in estudiantes:
            self.add_error('estudiantes', "El profesor no puede ser estudiante del curso.")    
        return cleaned_data


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
        
        elemento = Articulo.objects.all().values_list('pk', 'titulo').union(
            Tesis.objects.all().values_list('pk', 'titulo'),
            Resultado.objects.all().values_list('pk', 'titulo'),
            Proyecto.objects.all().values_list('pk', 'titulo')
        )

        self.fields['oponentes'].choices = trabajadores_personas_choices()
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
        self.fields['autores'].choices = trabajadores_personas_choices(trabajador=self.request.user.trabajador)


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
        self.fields['miembros'].choices = trabajadores_personas_choices(trabajador=self.request.user.trabajador)


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
        self.fields['integrantes'].choices = trabajadores_personas_choices()


class FormCrearTutoria(BSModalForm):

    class Meta:
        model = Tutoria
        exclude = ['tutor']
        widgets = {
            'fecha_inicio': DateInput(),
        }




