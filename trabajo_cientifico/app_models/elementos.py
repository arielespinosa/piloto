from django.db import models
from .nomencladores import *
#from human_resource.models import Persona


NIVEL_PUBLICACION = (
    ('GrupoI', 'GrupoI'),
    ('GrupoII', 'GrupoII'),
    ('GrupoIII', 'GrupoIII'),
    ('GrupoIV', 'GrupoIV'),)


PARTICIPACION_PUBLICACION = (
    ('Autor Principal1', 'Autor Principal'),
    ('Otro Autor', 'Otro Autor'),
    ('Colaborador', 'Colaborador'),)


class Articulo(models.Model):
    doi = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    #autores = models.ManyToManyField(Persona)
    db = models.CharField(max_length=100, null=True, blank=True)
    paginas = models.CharField(max_length=50)
    fecha_publicado = models.DateField()
    referencia_web = models.URLField(null=True, blank=True)
    revista = models.CharField(max_length=200)
    issn = models.CharField(max_length=50, null=True, blank=True)
    volumen = models.IntegerField()
    numero = models.IntegerField()
    impacto = models.FloatField()
    indexado = models.BooleanField(default=False)
    arbitrado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Libro(models.Model):
    isbn = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    #autores = models.ManyToManyField(Persona)
    base_datos = models.CharField(max_length=100, null=True, blank=True) # que es esto?
    paginas = models.CharField(max_length=50) # cant de paginas?
    fecha_publicado = models.DateField()
    referencia_web = models.URLField(null=True, blank=True)
    editorial = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    capitulo = models.CharField(max_length=50) # cant de capitulos?
    total_paginas = models.CharField(max_length=50) # no deberia ser entero?

    def __str__(self):
        return self.titulo


class LiteraturaGris(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=500)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo


class Resultado(models.Model):
    NIVEL = (
        ('1', 'Primer Nivel'),
        ('2', 'Segundo Nivel'),
        ('3', 'Tercer Nivel'),
    )

    titulo = models.CharField(max_length=200)
    #colectivo_de_autores = models.ManyToManyField(Persona)
    aprobado_cc = models.BooleanField(default=False)
    premios = models.ManyToManyField(Premio, null=True, blank=True)
    nivel = models.CharField(max_length=40, choices=NIVEL, null=True, blank=True)
 
    def __str__(self):
        return self.titulo


class Proyecto(models.Model):

    NIVEL_PROYECTO = (
        ('PP', 'Programa Priorizado'),
        ('PE','Proyecto Empresarial'),
        ('Ift', 'Institucional ft'),
        ('I','Institucional'),
    )

    TIPO_PROYECTO = (
        ('N', 'Nacional'),
        ('I', 'Internacional'),
    )

    centro_costo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=150)
    programa = models.ForeignKey(Programa, on_delete=models.DO_NOTHING, null=True, blank=True)
    #jefe = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, null=True, blank=True)
    dirigido_por_cfa = models.BooleanField(default=False)
    tipo = models.CharField(max_length=40, choices=TIPO_PROYECTO)
    nivel = models.CharField(max_length=40, choices=NIVEL_PROYECTO, blank=True, null=True)
    presupuesto_total = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    presupuesto_anno = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    entidad_ejecutora = models.ForeignKey(Entidad, on_delete=models.DO_NOTHING, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    resultados = models.ManyToManyField(Resultado, null=True, blank=True)
    entidades = models.ManyToManyField(Entidad, related_name="entidades_participantes", null=True, blank=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    TIPO_SCT = (
        ('Estatal', 'Estatal'),
        ('Comercial', 'Comercial'),
    )

    nombre = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_SCT, blank=True, null=True)
    dim = models.CharField(max_length=50, blank=True, null=True)
    centro_costo = models.CharField(max_length=50, blank=True, null=True)
    grupo = models.ForeignKey(GrupoTrabajo, on_delete=models.CASCADE, blank=True, null=True)
    #responsable = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    monto = models.IntegerField(default=0, blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, null=True, blank=True)
    resultados = models.ManyToManyField(Resultado)

    def __str__(self):
        return self.nombre
