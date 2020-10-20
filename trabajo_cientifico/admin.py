from django.contrib import admin
from .app_models.nomencladores import (
    Entidad, Cliente, GrupoTrabajo, Programa
)

from .app_models.elementos import (
    Proyecto, Servicio, Resultado, LiteraturaGris, Libro, Articulo
)

admin.register(Entidad)
admin.register(Proyecto)
admin.register(Servicio)
admin.register(Resultado)
admin.register(LiteraturaGris)
admin.register(Libro)
admin.register(Articulo)
admin.register(Cliente)
admin.register(GrupoTrabajo)
admin.register(Programa)



