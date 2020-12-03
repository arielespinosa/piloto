from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from trabajador.mixins import BSModalAjaxFormMixin
from trabajador.modelos.docencia import *
from trabajador.modelos.trabajo_cientifico import Tesis, Resultado, Proyecto, Articulo
from trabajador.formularios import docencia as forms


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
        form_seleccionar_eventos.fields['eventos'].queryset = Evento.objects.all().exclude(
            trabajador=self.request.user.trabajador)

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

                print(data['nuevo_evento'])
                return JsonResponse(data)
            else:
                return super(CrearEvento, self).post(request, *args, **kwargs)


class CrearCurso(BSModalCreateView):
    template_name = 'crud/crear_curso.html'
    form_class = forms.FormCrearCurso
    success_message = 'El curso se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearCurso, self).get_context_data(**kwargs)

        context.update({
            'form_crear_curso': self.get_form(self.form_class),
        })

        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        # Añadir el tribunales creado al trabajador. Hacerlo via formset mas adelante
        form_crear_curso = self.get_form(self.form_class)

        if form_crear_curso.is_valid():
            curso = form_crear_curso.save(commit=False)
            curso.save()
            return JsonResponse(data)
        else:
            return super(CrearCurso, self).post(request, *args, **kwargs)


class CrearCursoRealizado(BSModalCreateView):
    template_name = 'crud/crear_curso_realizado.html'
    form_seleccionar_curso = forms.FormSeleccionarCursos
    form_class = forms.FormCrearCursoRealizado
    success_message = 'El curso se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super(CrearCursoRealizado, self).get_context_data(**kwargs)

        # Establecer formulario para seleccionar tribunales existentes que el usuario no haya participado
        form_seleccionar_curso = self.form_seleccionar_curso(trabajador=self.request.user.trabajador)

        # Si hay Cursos en los que el trabajador no tiene, enviarlos al template
        if len(form_seleccionar_curso.fields['cursos'].choices) > 0:
            context.update({
                'form_seleccionar_curso': form_seleccionar_curso,
            })

        context.update({
            'form_crear_curso_realizado': self.get_form(self.form_class),
        })

        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
            'cursos': {},
        }

        # Añadir los cursos seleccionados al trabajador
        cursos_realizados = request.POST.getlist('cursos')
        if cursos_realizados:
            for curso_realizado_pk in cursos_realizados:
                curso = CursoRealizado.objects.get(pk=curso_realizado_pk)
                curso.estudiantes.add(request.user.trabajador)
                # data['cursos'].update(model_to_dict(curso))

        # Añadir el tribunales creado al trabajador. Hacerlo via formset mas adelante
        form_crear_curso_realizado = self.get_form(self.form_class)
        form_crear_curso_realizado.request = request
    
        if not form_crear_curso_realizado.is_empity:
            if form_crear_curso_realizado.is_valid():
                profesor_pk = request.POST.get('profesor')

                try:
                    profesor = Trabajador.objects.get(pk=profesor_pk)
                except:
                    profesor = PersonaExterna.objects.get(pk=profesor_pk)

                curso_realizado = form_crear_curso_realizado.save(commit=False)
                curso_realizado.edicion = CursoRealizado.objects.filter(curso__pk=curso_realizado.curso.pk).count() + 1
                curso_realizado.profesor = profesor
                curso_realizado.save()

                """
                # Añadir los estudiantes al curso
                estudiantes = request.POST.getlist('estudiantes')
                for estudiante_pk in estudiantes:
                    try:
                        miembro = Trabajador.objects.get(pk=miembro_pk)
                    except:
                        miembro = PersonaExterna.objects.get(pk=miembro_pk)
                    tribunal.miembros.add(miembro)
                tribunal.miembros.add(request.user.trabajador)



                data.update({
                    'nueva_certificacion': model_to_dict(certificacion),
                })
                """

                return JsonResponse(data)
            else:
                return super(CrearCursoRealizado, self).post(request, *args, **kwargs)


class CrearTribunal(BSModalCreateView):
    template_name = 'crud/crear_tribunal.html'
    form_class = forms.FormCrearTribunal
    form_seleccionar_tribunal = forms.FormTribunales
    success_message = 'El tribunal se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def to_dict(self, tribunal):
        tribunal = model_to_dict(tribunal, exclude=['miembros'])
        tribunal['tesis'] = Tesis.objects.get(pk=tribunal['tesis']).titulo
        return tribunal

    def get_context_data(self, **kwargs):
        context = super(CrearTribunal, self).get_context_data(**kwargs)

        # Establecer formulario para seleccionar tribunales existentes que el usuario no haya participado
        form_seleccionar_tribunal = self.form_seleccionar_tribunal(self.request.GET)
        form_seleccionar_tribunal.fields['tribunales'].queryset = Tribunal.objects.all()

        # Si hay Eventos en los que el trabajador no ha participado, enviarlos al template
        if form_seleccionar_tribunal.fields['tribunales'].queryset.count() > 0:
            context.update({
                'form_seleccionar_tribunal': form_seleccionar_tribunal,
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

        # Añadir los tribunales cesionados seleccionados al trabajador
        tribunales = request.POST.get('tribunales')
        if tribunales:
            for tribunal_pk in tribunales:
                tribunal = Tribunal.objects.get(pk=tribunal_pk)
                tribunal.miembros.add(request.user.trabajador)
                # data['tribunales'].update(model_to_dict(tribunal))

        # Añadir el tribunal creado al trabajador. Hacerlo via formset mas adelante
        form_crear_tribunal = self.get_form(self.form_class)
        form_crear_tribunal.request = request
        if not form_crear_tribunal.is_empity:
            if form_crear_tribunal.is_valid():
                tribunal = form_crear_tribunal.save(commit=False)
                tribunal.save()

                # Añadir los miembros de tribunal
                miembros = request.POST.getlist('miembros')
                for miembro_pk in miembros:
                    try:
                        miembro = Trabajador.objects.get(pk=miembro_pk)
                    except:
                        miembro = PersonaExterna.objects.get(pk=miembro_pk)
                    tribunal.miembros.add(miembro)
                tribunal.miembros.add(request.user.trabajador)

                data.update({
                    'nuevo_tribunal': self.to_dict(tribunal),
                })
                return JsonResponse(data)
            else:
                return super(CrearTribunal, self).post(request, *args, **kwargs)


class CrearOponencia(BSModalCreateView):
    template_name = 'crud/crear_oponencia.html'
    form_class = forms.FormCrearOponencia
    form_seleccionar_oponencias = forms.FormOponencias
    success_message = 'La oponencia se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    def to_dict(self, oponencia):
        _oponencia = model_to_dict(oponencia, exclude=['oponentes'])
        _oponencia['elemento'] = oponencia.elemento.titulo
        return _oponencia

    def get_context_data(self, **kwargs):
        context = super(CrearOponencia, self).get_context_data(**kwargs)

        # Establecer formulario para seleccionar ponencias existentes que el usuario no haya participado
        form_seleccionar_oponencias = self.form_seleccionar_oponencias(self.request.GET)
        #print(self.request.user.trabajador.oponencias.all())
        
        #for o in Oponencia.objects.all():
            #print(o.oponentes.all(exclude))
        
        #print(Oponencia.objects.all().exclude(oponentes__trabajador_pk=1))
        #form_seleccionar_oponencias.fields['oponencias'].queryset = Oponencia.objects.all().exclude(oponentes__pk=self.request.user.trabajador.pk)
        
        # Remove oponencias en las cuales ya el trabajador está
        form_seleccionar_oponencias.fields['oponencias'].queryset = Oponencia.objects.all()

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
            for oponencia_pk in oponencias:
                oponencia = Oponencia.objects.get(pk=oponencia_pk)
                request.user.trabajador.oponencias.add(oponencia)
                #data['oponencias'].update(model_to_dict(oponencia))

        # Añadir el tribunales creado al trabajador. Hacerlo via formset mas adelante
        form_crear_oponencia = self.get_form(self.form_class)
        form_crear_oponencia.request = request
        if not form_crear_oponencia.is_empity:
            if form_crear_oponencia.is_valid():
                elemento_pk = request.POST.get('elemento') 
                
                try:
                    elemento = Articulo.objects.get(pk=elemento_pk)
                except:
                    pass
                try:
                    elemento = Tesis.objects.get(pk=elemento_pk)
                except:
                    pass
                try:
                    elemento = Resultado.objects.get(pk=elemento_pk)
                except:
                    pass
                try:
                    elemento = Proyecto.objects.get(pk=elemento_pk)
                except:
                    pass
                
                oponencia = form_crear_oponencia.save(commit=False)
                oponencia.elemento = elemento
                oponencia.save()

                oponentes_pk = request.POST.getlist('oponentes')
                for pk in oponentes_pk:
                    try:
                        oponente = Trabajador.objects.get(pk=pk)
                    except:
                        oponente = PersonaExterna.objects.get(pk=pk)                
                    oponencia.oponentes.add(oponente)
                oponencia.oponentes.add(request.user.trabajador)
                
                if request.is_ajax():
                    data.update({
                        'nueva_oponencia': self.to_dict(oponencia),
                    })
                    return JsonResponse(data)
                else:
                    return redirect('/trabajador')
            else:
                return super(CrearOponencia, self).post(request, *args, **kwargs)


class CrearPonencia(BSModalCreateView):
    template_name = 'crud/crear_ponencia.html'
    form_class = forms.FormCrearPonencia
    form_seleccionar_ponencias = forms.FormPonencias
    form_crear_ponencia_realizada = forms.FormCrearPonenciaRealizada
    success_message = 'La ponencia se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    @staticmethod
    def to_dict(ponencia):
        _ponencia = model_to_dict(ponencia)
        _ponencia['ponencia'] = ponencia.ponencia.titulo

        evento = Evento.objects.get(pk=_ponencia['evento'])
        _ponencia['evento'] = evento.nombre
        _ponencia['fecha'] = evento.fecha

        return _ponencia

    def get_context_data(self, **kwargs):
        context = super(CrearPonencia, self).get_context_data(**kwargs)

        # Establecer formulario para seleccionar ponencias existentes que el usuario no haya participado
        form_seleccionar_ponencias = self.form_seleccionar_ponencias(self.request.GET)
        form_seleccionar_ponencias.fields['ponencias'].queryset = Ponencia.objects.all()
        
        # Si hay Eventos en los que el trabajador no ha participado, enviarlos al template
        if form_seleccionar_ponencias.fields['ponencias'].queryset.count() > 0:
            context.update({
                'form_seleccionar_ponencias': form_seleccionar_ponencias,
            })

        # Ofrecer siempre la posibilidad de crear un nuevo evento
        context.update({
            'form_crear_ponencia': self.get_form(self.form_class),
            'form_crear_ponencia_realizada': self.get_form(self.form_crear_ponencia_realizada)
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

        # Añadir Ponencia y PonenciaRealizada
        form_crear_ponencia = self.get_form(self.form_class)
        form_crear_ponencia_realizada = self.get_form(self.form_crear_ponencia_realizada)
        form_crear_ponencia.request = request
        form_crear_ponencia_realizada.request = request
        
        if not form_crear_ponencia.is_empity:
            if form_crear_ponencia.is_valid() and form_crear_ponencia_realizada.is_valid():
                ponencia = form_crear_ponencia.save(commit=False)
                ponencia.save()
                
                # Añadir autores a la Ponencia
                autores_pk = request.POST.getlist('autores')
                if autores_pk:
                    for pk in autores_pk:
                        try:
                            autor = Trabajador.objects.get(pk=pk)
                        except:
                            autor = PersonaExterna.objects.get(pk=pk)                
                        ponencia.autores.add(autor)
                ponencia.autores.add(request.user.trabajador)
                
                # Crear PonenciasRealizadas
                ponencia_realizada = form_crear_ponencia_realizada.save(commit=False)
                ponencia_realizada.ponencia = ponencia
                ponencia_realizada.ponente = request.user.trabajador
                ponencia_realizada.save()

                data.update({
                    'nueva_ponencia': self.to_dict(ponencia_realizada),
                })
                return JsonResponse(data)
            else:
                return super(CrearPonencia, self).post(request, *args, **kwargs)


class CrearTutoria(BSModalCreateView):
    template_name = 'crud/crear_tutoria.html'
    form_class = forms.FormCrearTutoria
    success_message = 'La tutoria se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    @staticmethod
    def to_dict(tutoria):
        _tutoria = model_to_dict(tutoria)
        _tutoria['tesis'] = tutoria.tesis.titulo
        return _tutoria

    def get_context_data(self, **kwargs):
        context = super(CrearTutoria, self).get_context_data(**kwargs)

        context.update({
            'form_crear_tutoria': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        # Añadir Tutoria
        form_crear_tutoria = self.get_form(self.form_class)
        form_crear_tutoria.request = request
      
        if form_crear_tutoria.is_valid():
            tutoria = form_crear_tutoria.save(commit=False)
            tutoria.tutor = request.user.trabajador
            tutoria.save()

            data.update({
                'nueva_tutoria': self.to_dict(tutoria),
            })
            return JsonResponse(data)
        else:
            return super(CrearTutoria, self).post(request, *args, **kwargs)


class CrearCertificarTrabajador(BSModalCreateView):
    template_name = 'crud/crear_certificar_trabajador.html'
    form_class = forms.FormCrearCertificarTrabajador
    success_message = 'El certificado se añadio satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')

    @staticmethod
    def to_dict(tutoria):
        _tutoria = model_to_dict(tutoria)
        _tutoria['tesis'] = tutoria.tesis.titulo
        return _tutoria

    def get_context_data(self, **kwargs):
        context = super(CrearCertificarTrabajador, self).get_context_data(**kwargs)

        context.update({
            'form_crear_certificacion': self.get_form(self.form_class),
        })
        return context

    def post(self, request, *args, **kwargs):
        data = {
            'title': "Notificación",
            'message': self.success_message,
        }

        form_crear_certificacion = self.get_form(self.form_class)
        form_crear_certificacion.request = request
      
        if form_crear_certificacion.is_valid():
            trabajador_certificacion = form_crear_certificacion.save(commit=False)
            trabajador_certificacion.trabajador = request.user.trabajador
            trabajador_certificacion.save()
            """
            data.update({
                'nueva_certificacion': self.to_dict(tutoria),
            })
            """
            return JsonResponse(data)
        else:
            return super(CrearCertificarTrabajador, self).post(request, *args, **kwargs)





class VerEvento(BSModalReadView):
    model = Evento
    template_name = 'crud/ver_evento.html'


class VerTribunal(BSModalReadView):
    model = Tribunal
    template_name = 'crud/ver_tribunal.html'

class VerOponencia(BSModalReadView):
    model = Oponencia
    template_name = 'crud/ver_oponencia.html'


class ModificarEvento(BSModalAjaxFormMixin, BSModalUpdateView):
    model = Evento
    template_name = 'crud/modificar_evento.html'
    form_class = forms.FormCrearEvento
    success_message = 'La nota meteorológica fue modificada satisfactoriamente.'


class EliminarEvento(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Evento
    template_name = 'eliminar_elemento.html'
    success_message = 'El evento fue eliminado de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')


class ListaEventos(ListView):
    template_name = 'eventos.html'

    def get_queryset(self):
        return Evento.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaEventos, self).get_context_data(**kwargs)
        context.update({
            'eventos': self.get_queryset,
        })
        return context


# Tribunal ----------------------------------



class EliminarTribunal(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Tribunal
    template_name = 'eliminar_elemento.html'
    success_message = 'El tribunal fue eliminado de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')


class ListaTribunales(ListView):
    template_name = 'tribunales.html'

    def get_queryset(self):
        return Tesis.objects.order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super(ListaTribunales, self).get_context_data(**kwargs)
        context.update({
            'tribunales': self.get_queryset,
        })
        return context


# Oponencias -------------------------------



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


# Tutoria -------------------------------

class EliminarTutoria(BSModalAjaxFormMixin, BSModalDeleteView):
    model = Tutoria
    template_name = 'eliminar_elemento.html'
    success_message = 'La Tutoria fue eliminada de su CV satisfactoriamente.'
    success_url = reverse_lazy('trabajador:perfil')


