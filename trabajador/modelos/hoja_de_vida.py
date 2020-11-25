from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .nomencladores import CentroEstudios

class Certificacion(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    titulo = models.CharField(max_length=100)
    profesor = GenericForeignKey('content_type', 'object_id')
    cantidad_horas = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    centro_estudios = models.ForeignKey(CentroEstudios, on_delete=models.DO_NOTHING)
    creditos = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo


