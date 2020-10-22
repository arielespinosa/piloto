from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import  HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from .mixins import BSModalAjaxFormMixin
from .models import *
from . import forms

def inicio(request):
    return render(request, 'docencia.html')


# Eventos ----------------------------------
class CrearEvento(BSModalCreateView):
    form_class = forms.FormCrearEvento
    form_seleccionar_eventos = forms.FormEventos
    template_name = 'crud/crear_evento.html'
    success_message = 'El evento se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearEvento, self).get_context_data(**kwargs)

        # Establecer formulario para seleccionar eventos existentes que el usuario no haya participado
        form_seleccionar_eventos = self.form_seleccionar_eventos(self.request.GET)
        form_seleccionar_eventos.fields['eventos'].queryset = Evento.objects.all().exclude(trabajador=self.request.user.trabajador)
        
        # Si hay Eventos en los que el trabajador no ha participado, enviarlos al template
        if form_seleccionar_eventos.fields['eventos'].queryset.count() > 0:
            context.update({
                'form_seleccionar_eventos': form_seleccionar_eventos,
            })

        # Ofrecer siempre la posibilidad de crear un nuevo evento
        context.update({
            'form_crear_evento': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'eventos': {},
        }

        # Añadir los eventos seleccionados al trabajador
        eventos = request.POST.getlist('eventos')
        if eventos:
            for evento_pk in eventos:
                evento = Evento.objects.get(pk=evento_pk)
                request.user.trabajador.eventos.add(evento)

                data['eventos'].update(model_to_dict(evento))

        # Añadir el evento creado al trabajador. Hacerlo via formset mas adelante
        form_crear_evento = self.form_class(request.POST)
        form_crear_evento.request = request
        if not form_crear_evento.is_empity:
            if form_crear_evento.is_valid():
                evento = form_crear_evento.save(commit=False)
                evento.save()
                request.user.trabajador.eventos.add(evento)
                
                data.update({
                    'nuevo_evento': model_to_dict(evento),
                })
                return JsonResponse(data)
            else:
                return super(CrearEvento, self).post(request, *args, **kwargs)

class VerEvento(BSModalReadView):
    model = Evento
    template_name = 'crud/ver_evento.html'

class EliminarEvento(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Evento
    template_name = 'eliminar_elemento.html'
    success_message = 'El evento fue eliminado de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

# Tesis ----------------------------------
class CrearTesis(BSModalCreateView):
    template_name = 'crud/crear_tesis.html'
    form_class = forms.FormCrearTesis
    success_message = 'La tesis se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearTesis, self).get_context_data(**kwargs)

        # Crear Tesis
        context.update({
            'form_crear_tesis': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'tesis': {},
        }

        # Añadir el evento creado al trabajador. Hacerlo via formset mas adelante
        form_crear_tesis = self.form_class(request.POST)
        form_crear_tesis.request = request
    
        if form_crear_tesis.is_valid():
            tesis = form_crear_tesis.save(commit=False)
            tesis.save()
            request.user.trabajador.tesis.add(tesis)
            
            data.update({
                'nueva_tesis': model_to_dict(tesis),
            })
            return JsonResponse(data)
        else:
            return super(CrearTesis, self).post(request, *args, **kwargs)

class VerTesis(BSModalReadView):
    model = Tesis
    template_name = 'crud/ver_tesis.html'

class EliminarTesis(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Tesis
    template_name = 'eliminar_elemento.html'
    success_message = 'La tesis fue eliminada de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

class ListaTesis(ListView):
    template_name = 'tesis.html'

    def get_queryset(self):
        return Tesis.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaTesis, self).get_context_data(**kwargs)
        context.update({
            'tesis': self.get_queryset,
        })
        return context


# Tribunal ----------------------------------
class CrearTribunal(BSModalAjaxFormMixin, BSModalCreateView):
    template_name = 'crud/crear_tribunal.html'
    form_class = forms.FormCrearTribunal
    form_seleccionar_tribunales = forms.FormTribunales
    success_message = 'El tribunal se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearTribunal, self).get_context_data(**kwargs)

        # Establecer formulario para seleccionar tribunales existentes que el usuario no haya participado
        form_seleccionar_tribunales = self.form_seleccionar_tribunales(self.request.GET)
        form_seleccionar_tribunales.fields['tribunales'].queryset = Tribunal.objects.all().exclude(trabajador=self.request.user.trabajador)
        
        # Si hay Eventos en los que el trabajador no ha participado, enviarlos al template
        if form_seleccionar_tribunales.fields['tribunales'].queryset.count() > 0:
            context.update({
                'form_seleccionar_tribunales': form_seleccionar_tribunales,
            })

        # Ofrecer siempre la posibilidad de crear un nuevo evento
        context.update({
            'form_crear_tribunal': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'tribunales': {},
        }

        # Añadir los tribunales seleccionados al trabajador
        tribunales = request.POST.getlist('tribunales')
        if tribunales:
            for tribunal_pk in tribunales:
                tribunal = Tribunal.objects.get(pk=tribunal_pk)
                request.user.trabajador.eventos.add(tribunal)

                data['tribunales'].update(model_to_dict(tribunal))

        # Añadir el tribunales creado al trabajador. Hacerlo via formset mas adelante
        form_crear_tribunal = self.form_class(request.POST)
        form_crear_tribunal.request = request
        if not form_crear_tribunal.is_empity:
            if form_crear_tribunal.is_valid():
                tribunal = form_crear_tribunal.save(commit=False)
                tribunal.save()
                request.user.trabajador.tribunal.add(tribunal)
                
                data.update({
                    'nuevo_tribunal': model_to_dict(tribunal),
                })
                return JsonResponse(data)
            else:
                return super(CrearTribunal, self).post(request, *args, **kwargs)

class VerTribunal(BSModalReadView):
    model = Tribunal
    template_name = 'crud/ver_tribunal.html'

class EliminarTribunal(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Tribunal
    template_name = 'eliminar_elemento.html'
    success_message = 'El tribunal fue eliminado de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

class ListaTribunal(ListView):
    template_name = 'tesis.html'

    def get_queryset(self):
        return Tesis.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaTesis, self).get_context_data(**kwargs)
        context.update({
            'tesis': self.get_queryset,
        })
        return context


# Certificaciones --------------------------------
class CrearCertificacion(BSModalCreateView):
    template_name = 'crud/crear_certificacion.html'
    form_seleccionar_certificacion = forms.FormCertificaciones
    form_class = forms.FormCrearCertificacion
    success_message = 'El evento se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    
    def get_context_data(self, **kwargs):
        context = super(CrearCertificacion, self).get_context_data(**kwargs)

        # Establecer formulario para seleccionar tribunales existentes que el usuario no haya participado
        form_seleccionar_certificacion = self.form_seleccionar_certificacion(self.request.GET)
        form_seleccionar_certificacion.fields['certificaciones'].queryset = Certificacion.objects.all().exclude(trabajador=self.request.user.trabajador)
        
        # Si hay Certificaciones en los que el trabajador no ha participado, enviarlos al template
        if form_seleccionar_certificacion.fields['certificaciones'].queryset.count() > 0:
            context.update({
                'form_seleccionar_certificacion': form_seleccionar_certificacion,
            })

        # Ofrecer siempre la posibilidad de crear un nuevo evento
        context.update({
            'form_crear_certificacion': self.get_form(self.form_class),
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
        form_crear_certificacion = self.form_class(request.POST)
        form_crear_certificacion.request = request
        if not form_crear_certificacion.is_empity:
            if form_crear_certificacion.is_valid():
                certificacion = form_crear_certificacion.save(commit=False)
                certificacion.save()
                request.user.trabajador.certificacion.add(certificacion)
                
                data.update({
                    'nueva_certificacion': model_to_dict(certificacion),
                })
                return JsonResponse(data)
            else:
                return super(CrearCertificacion, self).post(request, *args, **kwargs)

class VerCertificacion(BSModalReadView):
    model = Certificacion
    template_name = 'crud/ver_certificacion.html'

class EliminarCertificacion(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Certificacion
    template_name = 'eliminar_elemento.html'
    success_message = 'La certificacion fue eliminada de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

class ListaCertificaciones(ListView):
    template_name = 'certificaciones.html'

    def get_queryset(self):
        return Certificacion.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaCertificaciones, self).get_context_data(**kwargs)
        context.update({
            'certificaciones': self.get_queryset,
        })
        return context


# Ponencias -------------------------------
class CrearPonencia(BSModalCreateView):
    template_name = 'crud/crear_ponencia.html'
    form_class = forms.FormCrearPonencia
    form_seleccionar_ponencias = forms.FormPonencias
    success_message = 'La ponencia se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearPonencias, self).get_context_data(**kwargs)

        # Establecer formulario para seleccionar ponencias existentes que el usuario no haya participado
        form_seleccionar_ponencias = self.form_seleccionar_ponencias(self.request.GET)
        form_seleccionar_ponencias.fields['ponencias'].queryset = Ponencias.objects.all().exclude(trabajador=self.request.user.trabajador)
        
        # Si hay Eventos en los que el trabajador no ha participado, enviarlos al template
        if form_seleccionar_ponencias.fields['ponencias'].queryset.count() > 0:
            context.update({
                'form_seleccionar_ponencias': form_seleccionar_ponencias,
            })

        # Ofrecer siempre la posibilidad de crear un nuevo evento
        context.update({
            'form_crear_ponencia': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'ponencias': {},
        }

        # Añadir los tribunales seleccionados al trabajador
        ponencias = request.POST.getlist('ponencias')
        if ponencias:
            for ponencia_pk in ponencias:
                ponencia = Ponencia.objects.get(pk=ponencia_pk)
                request.user.trabajador.ponencias.add(ponencia)

                data['ponencias'].update(model_to_dict(ponencia))

        # Añadir el tribunales creado al trabajador. Hacerlo via formset mas adelante
        form_crear_ponencia = self.form_class(request.POST)
        form_crear_ponencia.request = request
        if not form_crear_ponencia.is_empity:
            if form_crear_ponencia.is_valid():
                ponencia = form_crear_ponencia.save(commit=False)
                ponencia.save()
                request.user.trabajador.ponencias.add(ponencia)
                
                data.update({
                    'nueva_ponencia': model_to_dict(ponencia),
                })
                return JsonResponse(data)
            else:
                return super(CrearPonencias, self).post(request, *args, **kwargs)

class VerPonencia(BSModalReadView):
    model = Ponencia
    template_name = 'crud/ver_ponencia.html'

class EliminarPonencia(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Ponencia
    template_name = 'eliminar_elemento.html'
    success_message = 'La Ponencia fue eliminada de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

class ListaPonencias(ListView):
    template_name = 'ponencias.html'

    def get_queryset(self):
        return Ponencia.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaPonencias, self).get_context_data(**kwargs)
        context.update({
            'ponencias': self.get_queryset,
        })
        return context


# Oponencias -------------------------------
class CrearOponencia(BSModalCreateView):
    template_name = 'crud/crear_oponencia.html'
    form_class = forms.FormCrearOponencia
    form_seleccionar_oponencias = forms.FormOponencias
    success_message = 'La oponencia se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearOponencia, self).get_context_data(**kwargs)

        # Establecer formulario para seleccionar ponencias existentes que el usuario no haya participado
        form_seleccionar_oponencias = self.form_seleccionar_oponencias(self.request.GET)
        form_seleccionar_oponencias.fields['oponencias'].queryset = Oponencia.objects.all().exclude(trabajador=self.request.user.trabajador)
        
        # Si hay Eventos en los que el trabajador no ha participado, enviarlos al template
        if form_seleccionar_oponencias.fields['oponencias'].queryset.count() > 0:
            context.update({
                'form_seleccionar_oponencias': form_seleccionar_oponencias,
            })

        # Ofrecer siempre la posibilidad de crear un nuevo evento
        context.update({
            'form_crear_oponencia': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'oponencias': {},
        }

        # Añadir los tribunales seleccionados al trabajador
        oponencias = request.POST.getlist('oponencias')
        if oponencias:
            for oponencia_pk in ponencias:
                oponencia = Oponencia.objects.get(pk=oponencia_pk)
                request.user.trabajador.oponencias.add(oponencia)

                data['oponencias'].update(model_to_dict(oponencia))

        # Añadir el tribunales creado al trabajador. Hacerlo via formset mas adelante
        form_crear_oponencia = self.form_class(request.POST)
        form_crear_oponencia.request = request
        if not form_crear_oponencia.is_empity:
            if form_crear_oponencia.is_valid():
                oponencia = form_crear_oponencia.save(commit=False)
                oponencia.save()
                request.user.trabajador.oponencias.add(oponencia)
                
                data.update({
                    'nueva_oponencia': model_to_dict(oponencia),
                })
                return JsonResponse(data)
            else:
                return super(CrearOponencia, self).post(request, *args, **kwargs)

class VerOponencia(BSModalReadView):
    model = Oponencia
    template_name = 'crud/ver_oponencia.html'

class EliminarOponencia(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Oponencia
    template_name = 'eliminar_elemento.html'
    success_message = 'La oponencia fue eliminada de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

class ListaOponencias(ListView):
    template_name = 'oponencias.html'

    def get_queryset(self):
        return Oponencia.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaOponencias, self).get_context_data(**kwargs)
        context.update({
            'oponencias': self.get_queryset,
        })
        return context


