from django.shortcuts import render
from django.forms.models import model_to_dict
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import JsonResponse
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from trabajador.mixins import BSModalAjaxFormMixin
from trabajador.modelos.nomencladores import Cliente, CampoEspecialidad, CentroEstudios
from trabajador.modelos.trabajo_cientifico import *
from trabajador.formularios import trabajo_cientifico as forms


# Tesis ----------------------------------
class CrearTesis(BSModalCreateView):
    template_name = 'crud/crear_tesis.html'
    form_class = forms.FormCrearTesis
    success_message = 'La tesis se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def to_dict(self, tesis):
        dict_tesis = model_to_dict(tesis, exclude=['graduado'])
        dict_tesis['especialidad'] = CampoEspecialidad.objects.get(pk=dict_tesis['especialidad']).nombre
        dict_tesis['lugar'] = CentroEstudios.objects.get(pk=dict_tesis['lugar']).nombre
        return dict_tesis

    def get_context_data(self, **kwargs):
        context = super(CrearTesis, self).get_context_data(**kwargs)

        context.update({
            'form_crear_tesis': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        # Añadir la tesis al trabajador.
        form_crear_tesis = self.get_form(self.form_class)
        form_crear_tesis.request = request
    
        if form_crear_tesis.is_valid():                   
            estudiante_pk = request.POST.get('estudiante')
                              
            try:
                estudiante = Trabajador.objects.get(pk=estudiante_pk)
            except:
                estudiante = PersonaExterna.objects.get(pk=estudiante_pk) 
        
            tesis = form_crear_tesis.save(commit=False)
            tesis.estudiante = estudiante
            tesis.save()

            for tutor_pk in request.POST.getlist('tutores'):
                try:
                    tutor = Trabajador.objects.get(pk=tutor_pk)
                except:
                    tutor = PersonaExterna.objects.get(pk=tutor_pk)
                tesis.tutores.add(tutor)

            for tutor in tesis.tutores.all():
                try:
                    if not tutor.tutorias.get(tesis=tesis): 
                        tutor.tutoria_set.create(
                            fecha_inicio=tesis.fecha_inicio,
                            tesis=tesis
                        )
                except:
                    pass
            
            data.update({
                'nueva_tesis': self.to_dict(tesis),
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
    template_name = 'crud/listar_tesis.html'

    def get_queryset(self):
        return Tesis.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaTesis, self).get_context_data(**kwargs)
        context.update({
            'tesis': self.get_queryset,
        })
        return context


class CrearProyecto(BSModalCreateView):
    template_name = 'crud/crear_proyecto.html'
    form_class = forms.FormCrearProyecto
    success_message = 'El proyecto se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def to_dict(self, proyecto):
        dict_proyecto = model_to_dict(proyecto, exclude=['participantes'])
        dict_proyecto['centro_costo'] = CentroCosto.objects.get(pk=dict_proyecto['centro_costo']).nombre

        if dict_proyecto['programa']:
            dict_proyecto['programa'] = Programa.objects.get(pk=dict_proyecto['programa']).nombre

        return dict_proyecto

    def get_context_data(self, **kwargs):
        context = super(CrearProyecto, self).get_context_data(**kwargs)
        context.update({
            'form_crear_proyecto': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        # Añadir el proyecto
        form_crear_proyecto = self.get_form(self.form_class)
        form_crear_proyecto.request = request

        if form_crear_proyecto.is_valid(): 
            jefe_pk = request.POST.get('jefe')
            try:
                jefe = Trabajador.objects.get(pk=jefe_pk)
            except:
                jefe = PersonaExterna.objects.get(pk=jefe_pk)

            proyecto = form_crear_proyecto.save(commit=False)
            proyecto.jefe = jefe       
            proyecto.save()

            # Añadir los participantes
            participantes = request.POST.getlist('participantes')
            for participante_pk in participantes:
                try:
                    participante = Trabajador.objects.get(pk=participante_pk)
                except:
                    participante = PersonaExterna.objects.get(pk=participante_pk)
                proyecto.participantes.add(participante)
            proyecto.participantes.add(request.user.trabajador)
          
            data.update({
                'nuevo_proyecto': self.to_dict(proyecto),
            })
            return JsonResponse(data)
        else:
            return super(CrearProyecto, self).post(request, *args, **kwargs)


class VerProyecto(BSModalReadView):
    model = Proyecto
    template_name = 'crud/ver_proyecto.html'


class EliminarProyecto(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Proyecto
    template_name = 'eliminar_elemento.html'
    success_message = 'El proyecto fue eliminado de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

"""
class ListaProyectos(ListView):
    template_name = 'tesis.html'

    def get_queryset(self):
        return Tesis.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaTesis, self).get_context_data(**kwargs)
        context.update({
            'tesis': self.get_queryset,
        })
        return context
"""


class CrearArticulo(BSModalCreateView):
    template_name = 'crud/crear_articulo.html'
    form_class = forms.FormCrearArticulo
    success_message = 'El articulo se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def to_dict(self, articulo):
        return model_to_dict(articulo, exclude=['autores'])
    
    def get_context_data(self, **kwargs):
        context = super(CrearArticulo, self).get_context_data(**kwargs)
        context.update({
            'form_crear_articulo': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
         }

        # Añadir el centro creado
        form_crear_articulo = self.form_class(request.POST)
        form_crear_articulo.request = request

        if form_crear_articulo.is_valid():            
            articulo = form_crear_articulo.save(commit=False)
            articulo.save()

            for autor_pk in request.POST.get('autores'):
                try:
                    autor = Trabajador.objects.get(pk=autor_pk)
                except:
                    autor = PersonaExterna.objects.get(pk=autor_pk)
                articulo.autores.add(autor)
            articulo.autores.add(request.user.trabajador)

            data.update({
                'nuevo_articulo': self.to_dict(articulo),
            })
            return JsonResponse(data)
        else:
            return super(CrearArticulo, self).post(request, *args, **kwargs)


class VerArticulo(BSModalReadView):
    model = Articulo
    template_name = 'crud/ver_articulo.html'


class EliminarArticulo(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Articulo
    template_name = 'eliminar_elemento.html'
    success_message = 'El artículofue eliminado de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')


class CrearLibro(BSModalCreateView):
    template_name = 'crud/crear_libro.html'
    form_class = forms.FormCrearLibro
    success_message = 'El tribunal se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def to_dict(self, proyecto):
        return model_to_dict(proyecto, exclude=['autores'])

    def get_context_data(self, **kwargs):
        context = super(CrearLibro, self).get_context_data(**kwargs)
        context.update({
            'form_crear_libro': self.get_form(self.form_class),
        })
        return context
    
    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'libro': {},
        }

        # Añadir el libro creado
        form_crear_libro = self.get_form(self.form_class)
        form_crear_libro.request = request

        if form_crear_libro.is_valid():            
            libro = form_crear_libro.save(commit=True)
            libro.save()

            for autor_pk in request.POST.get('autores'):
                try:
                    autor = Trabajador.objects.get(pk=autor_pk)
                except:
                    autor = PersonaExterna.objects.get(pk=autor_pk)
                libro.autores.add(autor)

            libro.autores.add(request.user.trabajador)

            data.update({
                'nuevo_libro': self.to_dict(libro),
            })
            return JsonResponse(data)
        else:
            return super(CrearLibro, self).post(request, *args, **kwargs)


class VerLibro(BSModalReadView):
    model = Libro
    template_name = 'crud/ver_libro.html'


class EliminarLibro(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Libro
    template_name = 'eliminar_elemento.html'
    success_message = 'El libro fue eliminado de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')


class CrearResultado(BSModalCreateView):
    template_name = 'crud/crear_resultado.html'
    form_class = forms.FormCrearResultado
    success_message = 'El resultado se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearResultado, self).get_context_data(**kwargs)
        context.update({
            'form_crear_resultado': self.get_form(self.form_class),
        })
        return context
    
    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'resultado': {},
        }

        # Añadir el centro creado
        form_crear_resultado = self.form_class(request.POST)
        form_crear_resultado.request = request

        if form_crear_resultado.is_valid():
            
            resultado = form_crear_resultado.save()
            resultado.save()
            request.user.trabajador.resultados.add(resultado)

            data.update({
                'resultado': model_to_dict(resultado),
            })
            return JsonResponse(data)
        else:
            return super(CrearResultado, self).post(request, *args, **kwargs)


class VerResultado(BSModalReadView):
    model = Resultado
    template_name = 'crud/ver_resultado.html'


class EliminarResultado(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Resultado
    template_name = 'eliminar_elemento.html'
    success_message = 'El resultado fue eliminado de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')


class CrearServicio(BSModalCreateView):
    template_name = 'crud/crear_servicio.html'
    form_class = forms.FormCrearServicio
    success_message = 'El servicio se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def to_dict(self, proyecto):
        modelo = model_to_dict(proyecto, exclude=['participantes'])
        modelo['centro_costo'] = CentroCosto.objects.get(pk=modelo['centro_costo']).nombre
        modelo['cliente'] = Cliente.objects.get(pk=modelo['cliente']).nombre
        return modelo

    def get_context_data(self, **kwargs):
        context = super(CrearServicio, self).get_context_data(**kwargs)
        context.update({
            'form_crear_servicio': self.get_form(self.form_class),
        })
        return context
    

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        # Añadir el centro creado
        form_crear_servicio = self.get_form(self.form_class)
        form_crear_servicio.request = request

        if form_crear_servicio.is_valid():
            responsable_pk = request.POST.get('responsable')
            try:
                responsable = Trabajador.objects.get(pk=responsable_pk)
            except:
                responsable = PersonaExterna.objects.get(pk=responsable_pk)

            servicio = form_crear_servicio.save(commit=False)
            servicio.responsable = responsable 
            servicio.save()

            # Añadir los participantes
            participantes = request.POST.getlist('participantes')
            for participante_pk in participantes:
                try:
                    participante = Trabajador.objects.get(pk=participante_pk)
                except:
                    participante = PersonaExterna.objects.get(pk=participante_pk)
                servicio.participantes.add(participante)
            servicio.participantes.add(request.user.trabajador)

            data.update({
                'nuevo_servicio':self.to_dict(servicio),
            })
            return JsonResponse(data)
        else:
            return super(CrearServicio, self).post(request, *args, **kwargs)


class VerServicio(BSModalReadView):
    model = Servicio
    template_name = 'crud/ver_servicio.html'


class EliminarServicio(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Servicio
    template_name = 'eliminar_elemento.html'
    success_message = 'El servicio fue eliminado de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')


