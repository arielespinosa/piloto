from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from .mixins import BSModalAjaxFormMixin
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from .models import Inventario, Local, Objeto
from . import forms


class Inicio(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return render(request, 'centro.html')
            else:
                return HttpResponseRedirect('/trabajador')
                #return redirect(request.user.trabajador)
                #return reverse("trabajador:perfil")
        return super(Inicio, self).dispatch(request, *args, **kwargs)


def plan_de_trabajo(request):
    return render(request, 'plan_de_trabajo.html')


# Objeto ----------------------------------------------------------------
class AddObjeto(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'crud/add_objeto.html'
    form_class = forms.FormObjeto
    success_message = 'El objeto se añadio satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)        

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ActualizarObjeto(BSModalAjaxFormMixin, BSModalUpdateView):
    model = Objeto
    template_name = 'crud/actualizar_objeto.html'
    form_class = forms.FormObjeto
    success_message = 'El objeto fue modificado satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

class ListaObjeto(ListView):
    paginate_by = 3
    template_name = 'crud/lista_objeto.html'

    def get_queryset(self):
        return Objeto.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListaObjeto, self).get_context_data(**kwargs)        
        context.update({
            'objetos': self.get_queryset,
        })
        return context

class DetalleObjeto(BSModalReadView):
    model = Objeto
    template_name = 'crud/detalle_local.html'

class EliminarObjeto(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Objeto
    template_name = 'eliminar_elemento.html'
    success_message = 'El objeto fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

# Local ------------------------------------------------------------------
class AddLocal(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'crud/crear_local.html'
    form_class = forms.FormLocal
    success_message = 'El local se añadio satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)        

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ActualizarLocal(BSModalAjaxFormMixin, BSModalUpdateView):
    model = Local
    template_name = 'crud/actualizar_local.html'
    form_class = forms.FormLocal
    success_message = 'El local fue modificado satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

class ListaLocal(ListView):
    paginate_by = 3
    template_name = 'local.html'

    def get_queryset(self):
        return Local.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListaLocal, self).get_context_data(**kwargs)        
        context.update({
            'locales': self.get_queryset,
        })
        return context

class DetalleLocal(BSModalReadView):
    model = Local
    template_name = 'crud/detalle_local.html'

class EliminarLocal(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Local
    template_name = 'crud/eliminar_elemento.html'
    success_message = 'El local fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

# Inventario --------------------------------------------------------------   
class AddInventario(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'crud/crear_inventario.html'
    form_class = forms.Inventario
    success_message = 'El inventario se añadio satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)        

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ActualizarInventario(BSModalAjaxFormMixin, BSModalUpdateView):
    model = Inventario
    template_name = 'crud/actualizar_inventario.html'
    form_class = forms.FormInventario
    success_message = 'El inventario fue modificado satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

class ListaInventario(ListView):
    paginate_by = 3
    template_name = 'crud/lista_inventario.html'

    def get_queryset(self):
        return Inventario.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListaInventario, self).get_context_data(**kwargs)        
        context.update({
            'inventario': self.get_queryset,
        })
        return context


class DetalleInventario(BSModalReadView):
    model = Inventario
    template_name = 'crud/detalle_inventario.html'


class EliminarInventario(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Inventario
    template_name = 'crud/eliminar_elemento.html'
    success_message = 'El inventario fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')
   




