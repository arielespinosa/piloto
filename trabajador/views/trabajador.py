from django.shortcuts import render, reverse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.generic import FormView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView
from bootstrap_modal_forms.generic import (
                                            BSModalCreateView,
                                            BSModalUpdateView,
                                            BSModalReadView,
                                            BSModalDeleteView,
                                        )

from trabajador.mixins import BSModalAjaxFormMixin
from trabajador.formularios import trabajador as frm_trabajador
from trabajador.modelos.trabajadores import Trabajador, PersonaExterna
from trabajador.modelos.trabajo_cientifico import Tesis
from trabajador.modelos.docencia import CursoRealizado, Curso
from django_pdfkit import PDFView


class TrabajadorCV(PDFView):
    template_name = "cv.html"
    form_class = frm_trabajador.FormPerfilTrabajador

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trabajador'] = self.request.user.trabajador        
        return context


class CrearPersonaExterna(BSModalCreateView):
    template_name = 'crud/crear_persona_externa.html'
    form_class = frm_trabajador.FormCrearPersonaExterna
    success_message = 'La persona se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearPersonaExterna, self).get_context_data(**kwargs)
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
            contacto = form.save()
            contacto.save()
            return JsonResponse(data)
        else:
            return super(CrearPersonaExterna, self).post(request, *args, **kwargs)


class CrearContacto(BSModalCreateView):
    template_name = 'crud/crear_contacto.html'
    form_class = frm_trabajador.FormCrearContacto
    success_message = 'El Contacto se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearContacto, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'Contacto': {},
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            contacto = form.save()
            contacto.save()

            data.update({
                'contacto': model_to_dict(contacto),
            })
            return JsonResponse(data)
        else:
            return super(CrearContacto, self).post(request, *args, **kwargs)


class CrearAreaInteres(BSModalCreateView):
    template_name = 'crud/crear_area_de_interes.html'
    form_class = frm_trabajador.FormCrearAreaInteres
    success_message = 'El area de interes se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearAreaInteres, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'area_de_interes': {},
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            area_de_interes = form.save()
            area_de_interes.save()

            data.update({
                'area_de_interes': model_to_dict(area_de_interes),
            })
            return JsonResponse(data)
        else:
            return super(CrearAreaInteres, self).post(request, *args, **kwargs)


class CrearMunicipio(BSModalCreateView):
    template_name = 'crud/crear_municipio.html'
    form_class = frm_trabajador.FormCrearMunicipio
    success_message = 'El municipio se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearMunicipio, self).get_context_data(**kwargs)
        context.update({
            'form': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'Municipio': {},
        }

        form = self.form_class(request.POST)
        form.request = request

        if form.is_valid():            
            municipio = form.save()
            municipio.save()

            data.update({
                'municipio': model_to_dict(municipio),
            })
            return JsonResponse(data)
        else:
            return super(CrearMunicipio, self).post(request, *args, **kwargs)


# Trabajador ----------------------------------
class PerfilTrabajador(FormView):
    template_name = "trabajador.html"
    form_class = frm_trabajador.FormPerfilTrabajador
    #success_url = reverse('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trabajador'] = self.request.user.trabajador
        
        #print(Tesis.objects.filter(content_type_id=self.request.user.trabajador.id).count())

        paginador_de_tesis = Paginator(Tesis.objects.filter(object_id=self.request.user.trabajador.id), 15)
        pagina_de_tesis = self.request.GET.get('page_tesis')

        paginador_de_tutorias = Paginator(self.request.user.trabajador.tesis_tutoradas.all(), 15)
        pagina_de_tutorias = self.request.GET.get('page_tutorias')

        paginador_de_ponencias = Paginator(self.request.user.trabajador.ponenciasrealizadas_set.all(), 15)
        pagina_de_ponencias = self.request.GET.get('page_ponencias')
        
        paginador_de_oponencias = Paginator(self.request.user.trabajador.oponencias.all(), 15)
        pagina_de_oponencias = self.request.GET.get('page_oponencias')

        paginador_de_cursos_impartidos = Paginator(CursoRealizado.objects.filter(object_id=self.request.user.trabajador.id), 15)
        pagina_de_cursos_impartidos = self.request.GET.get('page_cursos_impartidos')
        
        paginador_de_articulos = Paginator(self.request.user.trabajador.articulos.all(), 15)
        pagina_de_articulos = self.request.GET.get('page_articulos')
              
        paginador_de_libros = Paginator(self.request.user.trabajador.libros.all(), 15)
        pagina_de_libros = self.request.GET.get('page_libros')

        paginador_de_proyectos = Paginator(self.request.user.trabajador.proyectos.all(), 15)
        pagina_de_proyectos = self.request.GET.get('page_proyectos')

        paginador_de_tribunales = Paginator(self.request.user.trabajador.tribunales.all(), 15)
        pagina_de_tribunales = self.request.GET.get('page_tribunales')
        
        paginador_de_servicios = Paginator(self.request.user.trabajador.servicios.all(), 15)
        pagina_de_servicios = self.request.GET.get('page_servicios')

        if paginador_de_tesis.count > 0:
            context['tesis'] = paginador_de_tesis.get_page(pagina_de_tesis)    

        if paginador_de_libros.count > 0:
            context['libros'] = paginador_de_libros.get_page(pagina_de_libros)    

        if paginador_de_tutorias.count > 0:
            context['tutorias'] = paginador_de_tutorias.get_page(pagina_de_tutorias)    
      
        if paginador_de_tribunales.count > 0:
            context['tribunales'] = paginador_de_tribunales.get_page(pagina_de_tribunales)
       
        if paginador_de_proyectos.count > 0:
            context['proyectos'] = paginador_de_proyectos.get_page(pagina_de_proyectos)

        if paginador_de_articulos.count > 0:
            context['articulos'] = paginador_de_articulos.get_page(pagina_de_articulos)
       
        #if paginador_de_certificaciones.count > 0:
            #context['certificaciones'] = paginador_de_certificaciones.get_page(pagina_de_certificaciones)

        if paginador_de_oponencias.count > 0:
            context['oponencias'] = paginador_de_oponencias.get_page(pagina_de_oponencias)

        if paginador_de_cursos_impartidos.count > 0:
            context['cursos_impartidos'] = paginador_de_cursos_impartidos.get_page(pagina_de_cursos_impartidos)


        if paginador_de_ponencias.count > 0:
            context['ponencias'] = paginador_de_ponencias.get_page(pagina_de_ponencias)

        if paginador_de_servicios.count > 0:
            context['servicios'] = paginador_de_servicios.get_page(pagina_de_servicios)

        # Set eventos tab active by default
        context['active'] = 'tesis'

        active = self.request.GET.get('active')

        if pagina_de_articulos or active is 'articulos':
            context['active'] = 'articulos'
        elif pagina_de_tesis:
            context['active'] = 'tesis'
        elif pagina_de_libros:
            context['active'] = 'libros'
        #elif pagina_de_certificaciones:
            #context['active'] = 'certificaciones'
        elif pagina_de_oponencias:
            context['active'] = 'oponencias'
        elif pagina_de_proyectos:
            context['active'] = 'proyectos'
        elif pagina_de_servicios:
            context['active'] = 'servicios'
        elif pagina_de_tribunales:
            context['active'] = 'tribunales'
        
        return context


class ModificarTrabajador(BSModalUpdateView):
    model = Trabajador
    template_name = 'modificar_datos_personales.html'
    form_class = frm_trabajador.FormModificarDatosPersonales
    success_message = 'Sus datos personales fueron modificados satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def form_valid(self, form):
        response = super(ModificarTrabajador, self).form_valid(form)

        if self.request.is_ajax():     
            if form.is_valid():
                f = form.save(commit=False)
                f.save()
                datos = {
                    'title': "Notificación",
                    'message': self.success_message,
                    #'data': form.cleaned_data,
                }
            return JsonResponse(datos)
        else:
            return response



