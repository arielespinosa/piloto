from django.contrib import admin
from trabajador.modelos.trabajadores import *
from trabajador.modelos.nomencladores import *
from trabajador.modelos.docencia import *
from trabajador.modelos.trabajo_cientifico import *

admin.site.register(Persona)
admin.site.register(PersonaExterna)
admin.site.register(Oficina)
admin.site.register(Contacto)
admin.site.register(Municipio)
admin.site.register(OrganismoMasas)
admin.site.register(OrganismoPolitico)
admin.site.register(AreaInteres)
admin.site.register(Plaza)
admin.site.register(Especialidad)
admin.site.register(CampoEspecialidad)
admin.site.register(CentroCosto)
admin.site.register(Trabajador)

admin.site.register(Premio)
admin.site.register(PremioTrabajador)
admin.site.register(Entidad)
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Servicio)
admin.site.register(Resultado)
admin.site.register(Libro)
admin.site.register(Articulo)
admin.site.register(Cliente)
admin.site.register(Programa)
admin.site.register(PremioElementoCientifico)

admin.site.register(CentroEstudios)
admin.site.register(Evento)
admin.site.register(Certificacion)
admin.site.register(Oponencia)
admin.site.register(Tribunal)
admin.site.register(Tesis)
admin.site.register(Ponencia)


