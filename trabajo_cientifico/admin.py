from django.contrib import admin
from .models import (
    Entidad, Proyecto, Servicio, Resultado, LiteraturaGris, Libro, Articulo, Cliente, GrupoTrabajo, Programa
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



