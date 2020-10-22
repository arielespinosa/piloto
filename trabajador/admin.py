from django.contrib import admin
from .app_models.trabajador import *
from .app_models.nomencladores import *


admin.site.register(Persona)
admin.site.register(Oficina)
admin.site.register(Contacto)
admin.site.register(Municipio)
admin.site.register(OrganismoMasas)
admin.site.register(OrganismoPolitico)
admin.site.register(AreasInteres)
admin.site.register(Plaza)
admin.site.register(Trabajador)
