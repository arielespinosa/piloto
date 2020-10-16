from django import forms
from human_resource.models import Trabajador
from bootstrap_modal_forms.forms import BSModalForm


class FormPerfilTrabajador(forms.ModelForm):
    class Meta:
        model = Trabajador
        exclude = ['usuario']
