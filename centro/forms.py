from django import forms
from django.utils.translation import gettext_lazy as _
from bootstrap_modal_forms.forms import BSModalForm
from .models import Local, Objeto, Inventario


class FormLocal(BSModalForm):
    class Meta:
        model = Local
        fields = '__all__'


class FormObjeto(BSModalForm):
    class Meta:
        model = Objeto
        fields = '__all__'


class FormInventario(BSModalForm):
    class Meta:
        model = Inventario
        fields = '__all__'


    
