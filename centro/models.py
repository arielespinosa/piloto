from django.db import models
from trabajador.modelos.trabajadores import Trabajador
from trabajador.modelos.trabajo_cientifico import Proyecto


class Local(models.Model):
    nombre = models.CharField(max_length=10)
    identificador = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

class Objeto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    
    ESTADO_OBJETO = (
        ('B', 'Baja'),
        ('EU', 'En uso'),
        ('PB', 'Proceso de baja'),
        ('R', 'Roto'),
    )
    fecha = models.DateField()
    numero = models.CharField(max_length=30)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True)
    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100) # que es esto ?
    estado = models.CharField(max_length=20, choices=ESTADO_OBJETO)
    responsable = models.ForeignKey(Trabajador, on_delete=models.DO_NOTHING, null=True, blank=True) # cambie a responsable la variable
    proyecto = models.ForeignKey(Proyecto, on_delete=models.DO_NOTHING, null=True, blank=True)
    expediente_x = models.BooleanField(default=False)
    inventario_contable = models.BooleanField(default=False)
    medio_computacion = models.BooleanField(default=False)
    carta_prestamo_in = models.FileField(null=True, blank=True)
    carta_prestamo_out = models.FileField(null=True, blank=True)
    prestado = models.BooleanField(default=False)
    traslado = models.BooleanField(default=False)
    carta_traslado_lugar = models.FileField(null=True, blank=True)
    carta_traslado_economia = models.FileField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.numero


class Sindicato(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

        

