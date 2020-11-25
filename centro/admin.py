from django.contrib import admin
from .models import *
from .modelos.nomencladores import *

admin.site.register(Local)
admin.site.register(Objeto)
admin.site.register(Inventario)
admin.site.register(Lugar)

