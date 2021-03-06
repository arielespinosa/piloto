from django.forms.models import model_to_dict
from django.http import  JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from trabajador.mixins import BSModalAjaxFormMixin
from trabajador.modelos.nomencladores import *
from trabajador.formularios import nomencladores as forms


class CrearCertificacion(BSModalCreateView):
    template_name = 'crud/crear_certificacion.html'
    form_seleccionar_certificacion = forms.FormCertificaciones
    form_class = forms.FormCrearCertificacion
    success_message = 'La certificación se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearCertificacion, self).get_context_data(**kwargs)

        # Establecer formulario para seleccionar tribunales existentes que el usuario no haya participado
        form_seleccionar_certificacion = self.form_seleccionar_certificacion(self.request.GET)
        form_seleccionar_certificacion.fields['certificaciones'].queryset = Certificacion.objects.all()
        
        # Si hay Certificaciones en los que el trabajador no tiene, enviarlos al template
        if form_seleccionar_certificacion.fields['certificaciones'].queryset.count() > 0:
            context.update({
                'form_seleccionar_certificacion': form_seleccionar_certificacion,
            })

        # Ofrecer siempre la posibilidad de crear una nueva certificacion
        form_crear_certificacion = self.get_form(self.form_class)
        context.update({
            'form_crear_certificacion': form_crear_certificacion,
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'certificaciones': {},
        }

        # Añadir los tribunales seleccionados al trabajador
        certificaciones = request.POST.getlist('certificaciones')
        if certificaciones:
            for certificacion_pk in certificaciones:
                certificacion = Certificacion.objects.get(pk=certificacion_pk)
                request.user.trabajador.certificaciones.add(certificacion)

                data['certificaciones'].update(model_to_dict(certificacion))

        # Añadir el tribunales creado al trabajador. Hacerlo via formset mas adelante
        form_crear_certificacion = self.get_form(self.form_class)
        form_crear_certificacion.request = request
        if not form_crear_certificacion.is_empity:
            if form_crear_certificacion.is_valid():
                profesor_pk = request.POST.get('profesor')

                try:
                    profesor = Trabajador.objects.get(pk=profesor_pk)
                except:
                    profesor = PersonaExterna.objects.get(pk=profesor_pk)

                certificacion = form_crear_certificacion.save(commit=False)
                certificacion.profesor = profesor
               
                certificacion.save()
                request.user.trabajador.certificaciones.add(certificacion)
                
                data.update({
                    'nueva_certificacion': model_to_dict(certificacion),
                })
                return JsonResponse(data)
            else:
                return super(CrearCertificacion, self).post(request, *args, **kwargs)


class CrearPremio(BSModalCreateView):
    template_name = 'crud/crear_premio.html'
    form_class = forms.FormCrearPremio
    success_message = 'El premio se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearPremio, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            premio = form.save()
            premio.save()

            data.update({
                'premio': model_to_dict(premio),
            })
            return JsonResponse(data)
        else:
            return super(CrearPremio, self).post(request, *args, **kwargs)


class CrearEntidad(BSModalCreateView):
    template_name = 'crud/crear_entidad.html'
    form_class = forms.FormCrearEntidad
    success_message = 'La entidad se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearEntidad, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'entidad': {},
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            entidad = form.save()
            entidad.save()

            data.update({
                'entidad': model_to_dict(entidad),
            })
            return JsonResponse(data)
        else:
            return super(CrearEntidad, self).post(request, *args, **kwargs)


class CrearCentroEstudios(BSModalCreateView):
    form_class = forms.FormCrearCentroEstudios
    template_name = 'crud/crear_centro_de_estudios.html'
    success_message = 'El centro se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearCentroEstudios, self).get_context_data(**kwargs)
        context.update({
            'form_crear_centro_de_estudios': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'centro_de_estudios': {},
        }

        # Añadir el centro creado
        form_crear_centro_de_estudios = self.form_class(request.POST)
        form_crear_centro_de_estudios.request = request

        if form_crear_centro_de_estudios.is_valid():
            
            centro_de_estudios = form_crear_centro_de_estudios.save()
            centro_de_estudios.save()

            data.update({
                'centro_de_estudios': model_to_dict(centro_de_estudios),
            })
            return JsonResponse(data)
        else:
            return super(CrearCentroEstudios, self).post(request, *args, **kwargs)


class CrearPrograma(BSModalCreateView):
    template_name = 'crud/crear_programa.html'
    form_class = forms.FormCrearPrograma
    success_message = 'El programa se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearPrograma, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            programa = form.save()
            programa.save()

            data.update({
                'programa': model_to_dict(programa),
            })
            return JsonResponse(data)
        else:
            return super(CrearPrograma, self).post(request, *args, **kwargs)


class CrearCliente(BSModalCreateView):
    template_name = 'crud/crear_cliente.html'
    form_class = forms.FormCrearCliente
    success_message = 'El Cliente se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearCliente, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            cliente = form.save()
            cliente.save()

            data.update({
                'cliente': model_to_dict(cliente),
            })
            return JsonResponse(data)
        else:
            return super(CrearCliente, self).post(request, *args, **kwargs)


class CrearCentroCosto(BSModalCreateView):
    template_name = 'crud/crear_centro_de_costo.html'
    form_class = forms.FormCrearCentroCosto
    success_message = 'El Centro de Costo se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearCentroCosto, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            centro_de_costo = form.save()
            centro_de_costo.save()

            data.update({
                'centro_de_costo': model_to_dict(centro_de_costo),
            })
            return JsonResponse(data)
        else:
            return super(CrearCentroCosto, self).post(request, *args, **kwargs)


class CrearEspecialidad(BSModalCreateView):
    template_name = 'crud/crear_especialidad.html'
    form_class = forms.FormCrearEspecialidad
    form_campo = forms.FormCrearCampoEspecialidad
    success_message = 'La Especialidad se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearEspecialidad, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        form_especialidad = self.get_form(self.form_class)
        form_campo = self.get_form(self.form_campo)
        form_especialidad.request = request
        form_campo.request = request

        if form_especialidad.is_valid():            
            especialidad = form_especialidad.save(commit=False)
            if form_campo and form_campo.is_valid():
                especialidad.campo = form_campo.save()
            centro_de_costo.save()

            return JsonResponse(data)
        else:
            return super(CrearCentroCosto, self).post(request, *args, **kwargs)


"""
class CrearEspecialidad(BSModalCreateView):
    template_name = 'crud/crear_especialidad.html'
    form_class = forms.FormCrearEspecialidad
    success_message = 'La especialidad se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearEspecialidad, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            especialidad = form.save()
            especialidad.save()
            return JsonResponse(data)
        else:
            return super(CrearEspecialidad, self).post(request, *args, **kwargs)
"""


class VerCertificacion(BSModalReadView):
    model = Certificacion
    template_name = 'crud/ver_certificacion.html'


class EliminarCertificacion(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Certificacion
    template_name = 'eliminar_elemento.html'
    success_message = 'La certificacion fue eliminada de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')


class ListaCertificaciones(ListView):
    template_name = 'crud/listar_certificaciones.html'

    def get_queryset(self):
        return Certificacion.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaCertificaciones, self).get_context_data(**kwargs)
        context.update({
            'certificaciones': self.get_queryset,
        })
        return context


class VerCentroEstudios(BSModalReadView):
    model = CentroEstudios
    template_name = 'crud/ver_centro_de_estudios.html'


class EliminarCentroEstudios(BSModalAjaxFormMixin, BSModalDeleteView):
    model = CentroEstudios
    template_name = 'eliminar_elemento.html'
    success_message = 'El centro fue eliminado satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')


class ListaCentrosEstudios(ListView):
    template_name = 'centros_de_estudios.html'

    def get_queryset(self):
        return CentroEstudios.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListaCentroEstudios, self).get_context_data(**kwargs)
        context.update({
            'eventos': self.get_queryset,
        })
        return context



