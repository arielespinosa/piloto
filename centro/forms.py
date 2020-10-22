from django import forms
from django.utils.translation import gettext_lazy as _
from bootstrap_modal_forms.forms import BSModalForm
from .models import Local, Objeto, Inventario

class DateInput(forms.DateInput):
    input_type = 'date'


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


class FormCrearLocal(BSModalForm):
    class Meta:
        model = Local
        fields = '__all__'


class FormCrearObjeto(BSModalForm):
    class Meta:
        model = Objeto
        fields = '__all__'
           

class FormCrearInventario(BSModalForm):
    class Meta:
        model = Inventario
        exclude = ['carta_prestamo_in', 'carta_prestamo_out', 'prestado', 'traslado', 'carta_traslado_lugar', 'carta_traslado_economia']
       
        widgets = {
            'observaciones': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'fecha': DateInput(),
        }
    
