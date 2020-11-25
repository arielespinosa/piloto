from django import forms
from trabajador.modelos.trabajadores import ( Trabajador, PersonaExterna,
    Contacto, AreaInteres, Municipio)
from trabajador.modelos.hoja_de_vida import Certificacion
from bootstrap_modal_forms.forms import BSModalForm


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


class FormCrearCertificacion(BSModalForm):  
    profesor = forms.ChoiceField(choices=[])

    class Meta:
        model = Certificacion
        fields = [
            'titulo', 
            'cantidad_horas', 
            'fecha_inicio', 
            'fecha_terminacion', 
            'centro_estudios',
            'creditos', 
            'descripcion'
        ]

        widgets = {
            'fecha_terminacion': DateInput(),
            'fecha_inicio': DateInput(),
            'centro_estudios':forms.Select(attrs={'id': 'id_centro_estudios'}),
        }
    
    @property
    def is_empity(self):
        self.is_valid()
        print(self.clean())
        print(self.fields.keys())
        return False

    def __init__(self, *args, **kwargs):
        super(FormCrearCertificacion, self).__init__(*args, **kwargs)
        query = Trabajador.objects.all().exclude(pk=self.request.user.trabajador.pk).values_list('pk', 'nombre').union(
            PersonaExterna.objects.all().values_list('pk', 'nombre')
        )

        self.fields['profesor'].choices = list(query)


