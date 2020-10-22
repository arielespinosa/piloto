from django.shortcuts import render, reverse
from django.views.generic import FormView
from django.core.paginator import Paginator
from . import forms


class PerfilTrabajador(FormView):
    template_name = "trabajador.html"
    form_class = forms.FormPerfilTrabajador
    #success_url = reverse('trabajador:perfil')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trabajador'] = self.request.user.trabajador

        paginador_de_eventos = Paginator(self.request.user.trabajador.eventos.all(), 10)
        pagina_de_eventos = self.request.GET.get('page')

        paginador_de_tesis = Paginator(self.request.user.trabajador.tesis.all(), 10)
        pagina_de_tesis = self.request.GET.get('page')

        paginador_de_articulos = Paginator(self.request.user.trabajador.articulos.all(), 10)
        pagina_de_articulos = self.request.GET.get('page')

        paginador_de_certificaciones = Paginator(self.request.user.trabajador.certificaciones.all(), 10)
        pagina_de_certificaciones = self.request.GET.get('page')

        paginador_de_literatura_gris = Paginator(self.request.user.trabajador.literatura_gris.all(), 10)
        pagina_de_literatura_gris = self.request.GET.get('page')

        paginador_de_oponencias = Paginator(self.request.user.trabajador.oponencias.all(), 10)
        pagina_de_oponencias = self.request.GET.get('page')

        paginador_de_ponencias = Paginator(self.request.user.trabajador.ponencias.all(), 10)
        pagina_de_ponencias = self.request.GET.get('page')

        paginador_de_proyectos = Paginator(self.request.user.trabajador.proyectos.all(), 10)
        pagina_de_proyectos = self.request.GET.get('page')

        paginador_de_servicios = Paginator(self.request.user.trabajador.servicios.all(), 10)
        pagina_de_servicios = self.request.GET.get('page')

        paginador_de_tribunales = Paginator(self.request.user.trabajador.tribunales.all(), 10)
        pagina_de_tribunales = self.request.GET.get('page')

        paginador_de_ponencias = Paginator(self.request.user.trabajador.ponencias.all(), 10)
        pagina_de_ponencias = self.request.GET.get('page')


        if paginador_de_eventos.count > 0:
            context['eventos'] = paginador_de_eventos.get_page(pagina_de_eventos)

        if paginador_de_tesis.count > 0:
            context['tesis'] = paginador_de_tesis.get_page(pagina_de_tesis)

        if paginador_de_articulos.count > 0:
            context['articulos'] = paginador_de_articulos.get_page(pagina_de_articulos)

        if paginador_de_certificaciones.count > 0:
            context['certificaciones'] = paginador_de_certificaciones.get_page(pagina_de_certificaciones)


        if paginador_de_literatura_gris.count > 0:
            context['literatura_gris'] = paginador_de_literatura_gris.get_page(pagina_de_literatura_gris)


        if paginador_de_oponencias.count > 0:
            context['oponencias'] = paginador_de_oponencias.get_page(pagina_de_oponencias)

        if paginador_de_tribunales.count > 0:
            context['tribunales'] = paginador_de_tribunales.get_page(pagina_de_tribunales)

        if paginador_de_tesis.count > 0:
            context['tesis'] = paginador_de_tesis.get_page(pagina_de_tesis)

        if paginador_de_ponencias.count > 0:
            context['ponencias'] = paginador_de_ponencias.get_page(pagina_de_ponencias)
            
        return context



    