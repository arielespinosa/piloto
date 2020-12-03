from django import forms
from trabajador.modelos.nomencladores import *
from trabajador.modelos.trabajadores import Trabajador, PersonaExterna
from bootstrap_modal_forms.forms import BSModalForm


class DateInput(forms.DateInput):
    input_type = 'date'


class FormCertificaciones(forms.Form):
    certificaciones = forms.ModelMultipleChoiceField(label='Certificaciones que no posee', queryset=None, required=False)
    class Meta:
        fields = ['certificaciones']

        
class FormCrearCertificacion(BSModalForm):  

    class Meta:
        model = Certificacion
        fields = '__all__'
        
class FormCrearPremio(BSModalForm):
    class Meta:
        model = Premio
        fields = '__all__'

class FormCrearEntidad(BSModalForm):
    class Meta:
        model = Entidad
        fields = '__all__'

class FormCrearPrograma(BSModalForm):
    class Meta:
        model = Programa
        fields = '__all__'

class FormCrearCliente(BSModalForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class FormCrearCentroCosto(BSModalForm):
    class Meta:
        model = CentroCosto
        fields = '__all__'
        
class FormCrearCentroEstudios(BSModalForm):
    class Meta:
        model = CentroEstudios
        fields = '__all__'

class FormCrearEspecialidad(BSModalForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

class FormCrearCampoEspecialidad(BSModalForm):
    class Meta:
        model = CampoEspecialidad
        fields = '__all__'


class FormCrearPlaza(BSModalForm):
    class Meta:
        model = Plaza
        fields = '__all__'


class FormCrearOficina(BSModalForm):
    class Meta:
        model = Oficina
        fields = '__all__'


class FormCrearOrganismoMasas(BSModalForm):
    class Meta:
        model = OrganismoMasas
        fields = '__all__'


class FormCrearOrganismoPolitico(BSModalForm):
    class Meta:
        model = OrganismoPolitico
        fields = '__all__'