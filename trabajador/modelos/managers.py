from django.db import models

class ProyectoManager(models.Manager):
    
    def terminados(self):
        return super().get_queryset().filter(fecha_terminado__isnull=False)
    
    def en_desarrollo(self):
        return super().get_queryset()
        return [model for model in list(super().get_queryset()) if model.en_desarrollo]
