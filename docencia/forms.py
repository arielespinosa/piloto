import datetime
from CFA import settings
from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class FormEventos(forms.Form):
    eventos = forms.ModelMultipleChoiceField(label='Eventos en los que no ha participado', queryset=None, required=False)

    class Meta:
        fields = ['eventos']


class FormCertificaciones(forms.Form):
    certificaciones = forms.ModelMultipleChoiceField(label='Certificaciones que no posee', queryset=None, required=False)
    
    class Meta:
        fields = ['certificaciones']


class FormOponencias(forms.Form):
    oponencias = forms.ModelMultipleChoiceField(label='Oponencia en las que no ha participado', queryset=None, required=False)

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


class FormCrearCertificacion(BSModalForm):  
    class Meta:
        model = Certificacion
        fields = ['nombre', 'nombre_profesor', 'cantidad_horas', 
        'fecha_inicio', 'fecha_terminacion', 'centro_estudios',
        'creditos', 'descripcion']

        widgets = {
            'fecha_terminacion': DateInput(),
            'fecha_inicio': DateInput(),
        }
    
    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False


class FormCrearOponencia(BSModalForm):  
    class Meta:
        model = Oponencia
        fields = ['titulo', 'autor_principal', 'tipo', 'fecha']
        widgets = {
            'fecha': DateInput(),
        }

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False


class FormCrearTribunal(BSModalForm):
    class Meta:
        model = Tribunal
        fields = ['titulo', 'autor_principal', 'fecha']
        widgets = {
            'fecha': DateInput(),
        }

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False


class FormCrearTesis(BSModalForm):  
    class Meta:
        model = Tesis
        fields = ['grado', 'especialidad', 'titulo', 'autor',
        'lugar', 'fecha']
        widgets = {
            'fecha': DateInput(),
        }

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False


class FormCrearPonencia(BSModalForm):  
 
    class Meta:
        model = Ponencia
        fields = ['evento', 'titulo', 'participacion', 'autores']

    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False

