from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
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
class CrearObjeto(BSModalCreateView):
    template_name = 'crud/crear_objeto.html'
    form_class = forms.FormCrearObjeto
    success_message = 'El objeto se añadio satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

    def get_context_data(self, **kwargs):
        context = super(CrearObjeto, self).get_context_data(**kwargs)

        context.update({
            'form_crear_objeto': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,            
        }

        form_crear_objeto = self.form_class(request.POST)
        form_crear_objeto.request = request
       
        if form_crear_objeto.is_valid():
            objeto = form_crear_objeto.save(commit=False)
            objeto.save()

            if request.is_ajax():
                return JsonResponse(data)
            else:
                return super(CrearObjeto, self).form_valid(form_crear_objeto)
        else:
            return super(CrearObjeto, self).post(request, *args, **kwargs)


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
class CrearLocal(BSModalCreateView):
    template_name = 'crud/crear_local.html'
    form_class = forms.FormCrearLocal
    success_message = 'El local se añadio satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

    def get_context_data(self, **kwargs):
        context = super(CrearLocal, self).get_context_data(**kwargs)

        context.update({
            'form_crear_local': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,            
        }

        form_crear_local = self.form_class(request.POST)
        form_crear_local.request = request
       
        if form_crear_local.is_valid():
            local = form_crear_local.save(commit=False)
            local.save()

            return JsonResponse(data)
        else:
            return super(CrearLocal, self).post(request, *args, **kwargs)


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
class CrearInventario(BSModalCreateView):
    template_name = 'crud/crear_inventario.html'
    form_class = forms.FormCrearInventario
    success_message = 'El inventario se añadio satisfactoriamente.'
    success_url = reverse_lazy('centro:inicio')

    def get_context_data(self, **kwargs):
        context = super(CrearInventario, self).get_context_data(**kwargs)

        context.update({
            'form_crear_inventario': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,            
        }

        form_crear_inventario = self.form_class(request.POST)
        form_crear_inventario.request = request
       
        if form_crear_inventario.is_valid():
            inventario = form_crear_inventario.save(commit=False)
            inventario.save()

            return JsonResponse(data)
        else:
            return super(CrearInventario, self).post(request, *args, **kwargs)


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
   




