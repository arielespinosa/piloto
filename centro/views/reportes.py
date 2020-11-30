import datetime as dt
from django.db import models
from django_pdfkit import PDFView
from trabajador.modelos.trabajo_cientifico import *
from trabajador.modelos.docencia import *

class BalanceAnual(PDFView):
    template_name = "reportes/balance_anual.html"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = dt.datetime.now()
        context['proximo_ano'] = current_time.year+1
        #context['proyectos_terminados'] = Proyecto.objects.filter(fecha_terminado__isnull=False)
        #context['proyectos_en_desarrollo'] = Proyecto.manager.en_desarrollo() 
        #context['proyectos_internacionales'] = Proyecto.objects.filter(programa='I') 
        context['proyectos'] = Proyecto.objects.filter(fecha_terminacion__gt=dt.datetime(current_time.year-1, 1, 1))
        context['resultados'] = Resultado.objects.filter(fecha__year=current_time.year)
        context['publicaciones'] = Articulo.objects.filter(fecha_publicado__year=current_time.year)
        context['eventos'] = Evento.objects.filter(fecha__year=current_time.year)
        context['servicios'] = Servicio.objects.all()
        context['premios'] = PremioElementoCientifico.objects.all()





        return context
