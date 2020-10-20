from django.shortcuts import render
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from .mixins import BSModalAjaxFormMixin
from .app_models.elementos import (Proyecto)
from . import forms

def inicio(request):
    return render(request, 'trabajo_cientifico.html')


class CrearProyecto(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'crud/crear_proyecto.html'
    form_class = forms.FormProyecto
    success_message = 'El proyecto se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        #form.fields['proyectos'].queryset = Proyecto.objects.all() #.exclude(trabajador=request.user.trabajador)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CrearArticulo(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'crud/crear_articulo.html'
    form_class = forms.FormArticulo
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('trabajador:perfil')

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        return render(request, self.template_name, {'form': form})


class CrearLibro(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'crud/crear_libro.html'
    form_class = forms.FormLibro
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('trabajador:perfil')

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        return render(request, self.template_name, {'form': form})


class CrearLiteraturaGris(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'crud/crear_literatura_gris.html'
    form_class = forms.FormLiteraturaGris
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('trabajador:perfil')

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        return render(request, self.template_name, {'form': form})


class CrearResultado(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'crud/crear_resultado.html'
    form_class = forms.FormResultado
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('trabajador:perfil')

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        return render(request, self.template_name, {'form': form})


class CrearServicio(BSModalCreateView):
    template_name = 'crud/crear_servicio.html'
    form_class = forms.FormServicio
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('trabajador:perfil')

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        return render(request, self.template_name, {'form': form})






