from django import forms
from trabajador.modelos.trabajadores import ( Trabajador, PersonaExterna,
    Contacto, AreaInteres, Municipio)
from trabajador.modelos.docencia import Certificacion
from bootstrap_modal_forms.forms import BSModalForm
from .utils import trabajadores_personas_choices


class DateInput(forms.DateInput):
    input_type = 'date'


class FormCrearAreaInteres(BSModalForm):
    class Meta:
        model = AreaInteres
        fields = '__all__'


class FormCrearMunicipio(BSModalForm):
    class Meta:
        model = Municipio
        fields = '__all__'

class FormCrearContacto(BSModalForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class FormCrearPersonaExterna(BSModalForm):
    class Meta:
        model = PersonaExterna
        fields = '__all__'

class FormPerfilTrabajador(forms.ModelForm):
    class Meta:
        model = Trabajador
        exclude = ['usuario']


class FormModificarDatosPersonales(BSModalForm):
    class Meta:
        model = Trabajador
        fields = '__all__'
        help_texts = {
            'nombre': 'El nombre es sensible a las mayúsculas',
        }


# ------------------------------ Hoja de Vida
class FormCertificaciones(forms.Form):
    certificaciones = forms.ModelMultipleChoiceField(label='Certificaciones que no posee', queryset=None, required=False)
    
    class Meta:
        fields = ['certificaciones']


