from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
import django
from .trabajadores import Trabajador, PersonaExterna
from .nomencladores import *
from .managers import *
import datetime


class ElementoCientifico(models.Model):
    titulo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.titulo


class Tesis(ElementoCientifico):
    GRADO_ESCOLAR = (
        ('S', 'Superior'),
        ('MSc', 'Master'),
        ('Dr', 'Doctorado'),
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    grado = models.CharField(max_length=3, choices=GRADO_ESCOLAR)
    especialidad = models.ForeignKey(CampoEspecialidad, on_delete=models.DO_NOTHING)
    lugar = models.ForeignKey(CentroEstudios, on_delete=models.DO_NOTHING)
    fecha_inicio = models.DateField(default=django.utils.timezone.now)
    fecha_culminacion = models.DateField(null=True, blank=True)
    estudiante = GenericForeignKey('content_type', 'object_id')
    tutores = GM2MField(Trabajador, PersonaExterna, related_name='tesis_tutoradas')

    @property
    def en_curso(self):
        return True if not fecha_inicio else False


class Articulo(ElementoCientifico):
    NIVEL = (
        ('I',  'Grupo I'),
        ('II', 'Grupo II'),
        ('III', 'Grupo III'),
        ('IV', 'Grupo IV'),
    )

    PARTICIPACION = (
        ('AP', 'Autor Principal'),
        ('OA', 'Otro Autor'),
    )

    ARBITRADO = (
        ('1', 'Si'),
        ('2', 'No'),
    )


    STATUS = (
        ('1', 'Enviado'),
        ('2', 'En revision'),
        ('3', 'Aceptado'),
    )

    doi = models.CharField(max_length=50, unique=True)
    autores = GM2MField(Trabajador, PersonaExterna, related_name='articulos')
    db = models.CharField(max_length=100, null=True, blank=True)
    paginas = models.CharField(max_length=50)
    fecha_publicado = models.DateField(default=django.utils.timezone.now, null=True)
    referencia_web = models.URLField(null=True, blank=True)
    revista = models.CharField(max_length=200)
    issn = models.CharField(max_length=50, unique=True)
    volumen = models.PositiveSmallIntegerField()
    numero = models.PositiveSmallIntegerField()
    impacto = models.CharField(max_length=50, choices=NIVEL)
    participacion = models.CharField(max_length=50, choices=PARTICIPACION)
    indexado = models.BooleanField(default=False)
    arbitrado = models.CharField(max_length=20, choices=ARBITRADO)
    literatura_gris = models.BooleanField(default=False)


class Resultado(ElementoCientifico):
    NIVEL = (
        ('1', 'Primer Nivel'),
        ('2', 'Segundo Nivel'),
        ('3', 'Tercer Nivel'),
    )
    fecha = models.DateField(default=django.utils.timezone.now)
    dirigido_por_cfa = models.BooleanField(default=True)
    aprobado_cc = models.BooleanField(default=False)
    premios = models.ManyToManyField(Premio, null=True, blank=True)
    nivel = models.CharField(max_length=40, choices=NIVEL)


class Proyecto(ElementoCientifico):
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
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    centro_costo = models.ForeignKey(CentroCosto, on_delete=models.DO_NOTHING)
    programa = models.ForeignKey(Programa, on_delete=models.DO_NOTHING, null=True, blank=True)
    jefe = GenericForeignKey('content_type', 'object_id')
    participantes = GM2MField(Trabajador, PersonaExterna, related_name='proyectos')
    dirigido_por_cfa = models.BooleanField(default=False)
    tipo = models.CharField(max_length=40, choices=TIPO_PROYECTO)
    nivel = models.CharField(max_length=40, choices=NIVEL_PROYECTO, blank=True, null=True)
    presupuesto_total = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    presupuesto_anno = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    fecha_aprobado = models.DateField(default=datetime.datetime.now())
    fecha_inicio = models.DateField(default=datetime.datetime.now())
    fecha_terminacion = models.DateField()
    fecha_terminado = models.DateField(null=True, blank=True)
    entidadejecutora = models.ForeignKey(Entidad, on_delete=models.DO_NOTHING, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    resultados = models.ManyToManyField(Resultado, null=True, blank=True)
    entidades = models.ManyToManyField(Entidad, related_name="entidades_participantes", null=True, blank=True)
    manager = ProyectoManager()

    @property
    def en_desarrollo(self):
        return True if not self.fecha_terminado else False

    @property
    def en_atraso(self):
        return True if not self.fecha_terminado and self.fecha_terminacion > datetime.datetime.now() else False
    
    def para_proximo_ano(self):
        return True if self.fecha_aprobado.year > datetime.datetime.now().year else False
        

class Libro(ElementoCientifico):
    isbn = models.CharField(max_length=50)
    autores = GM2MField(Trabajador, PersonaExterna, related_name='libros')
    base_datos = models.CharField(max_length=100, null=True, blank=True) # que es esto?
    paginas = models.CharField(max_length=50) # cant de paginas?
    fecha_publicado = models.DateField(default=django.utils.timezone.now)
    referencia_web = models.URLField(null=True, blank=True)
    editorial = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    capitulo = models.CharField(max_length=50) # cant de capitulos?
    total_paginas = models.CharField(max_length=50) # no deberia ser entero?
    literatura_gris = models.BooleanField(default=False)





class Servicio(models.Model):
    TIPO = (
        ('ES', 'Estatal'),
        ('C', 'Comercial'),
        ('EX', 'Exportación'),
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    fecha_inicio = models.DateField(default=django.utils.timezone.now())
    fecha_terminacion = models.DateField()
    nombre = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO, blank=True, null=True)
    dim = models.CharField(max_length=50, blank=True, null=True)
    centro_costo = models.ForeignKey(CentroCosto, on_delete=models.DO_NOTHING)
    participantes = GM2MField(Trabajador, PersonaExterna, related_name='servicios')
    responsable = GenericForeignKey('content_type', 'object_id')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    monto = models.FloatField(default=0.0)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, null=True, blank=True)
    resultados = models.ManyToManyField(Resultado, null=True, blank=True)
    tareas = models.ManyToManyField(Tarea, null=True, blank=True)

    def __str__(self):
        return self.nombre


class PremioElementoCientifico(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    fecha = models.DateField()
    premio = models.ForeignKey(Premio, on_delete=models.DO_NOTHING)
    elemento = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.premio.nombre