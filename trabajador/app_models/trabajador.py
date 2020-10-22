import django
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .nomencladores import *
from trabajo_cientifico.app_models.elementos import (
    Articulo, Libro, LiteraturaGris, Proyecto, Resultado, Servicio
)
from docencia.models import (
    Oponencia, Evento, Certificacion, Ponencia, Tesis, Tribunal
)


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Trabajador(Persona):
    CATEGORIA_OCUPACIONAL= (
        ('T', 'Técnico'),
        ('E', 'Especialista'),
    )

    ESPECIALIDAD = (
        ('T', 'Técnico'),
        ('E', 'Especialista'),
    )

    TIPO_PLANTILLA = (
        ('AP', 'A prueba'),
        ('F', 'Fijo'),)

    SEXO = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),)

    RAZA = (
        ('B', 'Blanca'),
        ('M', 'Mestiza'),
        ('N', 'Negra'),)

    NIVEL_ESCOLAR = (
        ('TM', 'Técnico Medio'),
        ('S', 'Superior'),)

    GRADO_CIENTIFICO = (
        ('MSc', 'Master en Ciencias'),
        ('Dr', 'Doctor en Ciencias'),)

    CATEGORIA_CIENTIFICA = (
        ('AI', 'Aspirante a Investigador'),
        ('IA', 'Investigador Agregado'),
        ('IT', 'Investigador Titular'),)

    CATEGORIA_DOCENTE = (
        ('PX', 'Profesor Auxiliar'),
        ('PA', 'Profesor Agregado'),
        ('PT', 'Profesor Titular'),
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_de_perfiles', default='avatar_default.jpg', null=True)
    ci = models.CharField(max_length=11)
    sexo = models.CharField(max_length=20, choices=SEXO)
    raza = models.CharField(max_length=20, choices=RAZA)
    nivel_escolar = models.CharField(max_length=50, choices=NIVEL_ESCOLAR)
    especialidad = models.CharField(max_length=50, choices=ESPECIALIDAD)
    grado_cientifico = models.CharField(max_length=50, choices=GRADO_CIENTIFICO, null=True, blank=True)
    cateogoria_cientifica = models.CharField(max_length=50, choices=CATEGORIA_CIENTIFICA, null=True, blank=True)
    cateogoria_docente = models.CharField(max_length=50, choices=CATEGORIA_DOCENTE, null=True, blank=True)
    
    tarjeta = models.IntegerField()
    plaza = models.ForeignKey(Plaza, on_delete=models.DO_NOTHING)
    oficina = models.ForeignKey(Oficina, on_delete=models.DO_NOTHING, null=True, blank=True)
    categoria_ocupacional = models.CharField(max_length=20, choices=CATEGORIA_OCUPACIONAL)
    fecha_entrada_insmet = models.DateField(default=django.utils.timezone.now)
    fecha_salida = models.DateField(null=True, blank=True)
    motivos_salida = models.TextField(max_length=1000, blank=True)

    res_34_19 = models.FloatField(null=True, blank=True)
    msc_dr = models.FloatField(null=True, blank=True)  # Lo que cobra por ser mst o phd
    otros_pagos_antiguo = models.FloatField(null=True, blank=True)
    otros_pagos_actual = models.FloatField(null=True, blank=True)
    #salario_total_antiguo = models.FloatField(blank=True, null=True)
    #salario_total_actual = models.FloatField(default=0, blank=True, null=True)

    direccion = models.CharField(max_length=200)
    municipio = models.ForeignKey(Municipio, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    membresias = models.ManyToManyField(OrganismoPolitico, blank=True)
    afiliaciones = models.ManyToManyField(OrganismoMasas, blank=True)

    areas_de_interes = models.ManyToManyField(AreasInteres, blank=True)
    contacto = models.ManyToManyField(Contacto, blank=True)
    proyectos = models.ManyToManyField(Proyecto, blank=True)

    servicios = models.ManyToManyField(Servicio, blank=True)
    libros = models.ManyToManyField(Libro, blank=True)
    articulos = models.ManyToManyField(Articulo, blank=True)
    literatura_gris = models.ManyToManyField(LiteraturaGris, blank=True)
    certificaciones = models.ManyToManyField(Certificacion, blank=True)
    ponencias = models.ManyToManyField(Ponencia, blank=True)
    oponencias = models.ManyToManyField(Oponencia, blank=True)
    tesis = models.ManyToManyField(Tesis, blank=True)
    tribunales = models.ManyToManyField(Tribunal, blank=True)
    eventos = models.ManyToManyField(Evento, blank=True)
    resultados = models.ManyToManyField(Resultado, blank=True)

    def __str__(self):
        return self.nombre

    @property
    def nombre_coloquial(self):
        if self.grado_cientifico:
            return self.grado_cientifico +' '+ self.nombre +' '+ self.apellido1 +' '+ self.apellido2
        return self.nombre +' '+ self.apellido1 +' '+ self.apellido2

    @property
    def fecha_nacimiento(self):
        return datetime(1991, 11, 28)
    
    @property
    def salario_total_antiguo(self):
        return 7

    @property
    def salario_total_actual(self):
        return 7

    @property
    def diferencia_salarial(self):
        return 7
    """
    def get_absolute_url(self):
        return reverse("recursos_humanos:perfil_trabajador", kwargs={"id":self.id})
    """



