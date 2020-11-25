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
from trabajador.modelos.hoja_de_vida import Certificacion
from trabajador.modelos.trabajo_cientifico import Tesis
from django_pdfkit import PDFView


class TrabajadorCV(PDFView):
    template_name = "cv.html"
    form_class = frm_trabajador.FormPerfilTrabajador

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trabajador'] = self.request.user.trabajador        
        return context


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

        paginador_de_tutorias = Paginator(self.request.user.trabajador.tutorias.all(), 15)
        pagina_de_tutorias = self.request.GET.get('page_tutorias')

        paginador_de_ponencias = Paginator(self.request.user.trabajador.ponenciasrealizadas_set.all(), 15)
        pagina_de_ponencias = self.request.GET.get('page_ponencias')
        
        paginador_de_oponencias = Paginator(self.request.user.trabajador.oponencias.all(), 15)
        pagina_de_oponencias = self.request.GET.get('page_oponencias')

        paginador_de_certificaciones = Paginator(self.request.user.trabajador.certificaciones.all(), 15)
        pagina_de_certificaciones = self.request.GET.get('page_certificaciones')
        
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
       
        if paginador_de_certificaciones.count > 0:
            context['certificaciones'] = paginador_de_certificaciones.get_page(pagina_de_certificaciones)

        if paginador_de_oponencias.count > 0:
            context['oponencias'] = paginador_de_oponencias.get_page(pagina_de_oponencias)

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
        elif pagina_de_certificaciones:
            context['active'] = 'certificaciones'
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


# Hoja de vida ----------------------------------------------
class CrearCertificacion(BSModalCreateView):
    template_name = 'crud/crear_certificacion.html'
    form_seleccionar_certificacion = frm_trabajador.FormCertificaciones
    form_class = frm_trabajador.FormCrearCertificacion
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
    

