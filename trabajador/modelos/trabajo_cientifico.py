from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
import django
from .trabajadores import Trabajador, PersonaExterna
from .nomencladores import *
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
        ('C', 'Colaborador'),
    )

    doi = models.CharField(max_length=50, unique=True)
    autores = GM2MField(Trabajador, PersonaExterna, related_name='articulos')
    db = models.CharField(max_length=100, null=True, blank=True)
    paginas = models.CharField(max_length=50)
    fecha_publicado = models.DateField(default=django.utils.timezone.now)
    referencia_web = models.URLField(null=True, blank=True)
    revista = models.CharField(max_length=200)
    issn = models.CharField(max_length=50, unique=True)
    volumen = models.PositiveSmallIntegerField()
    numero = models.PositiveSmallIntegerField()
    impacto = models.CharField(max_length=50, choices=NIVEL)
    participacion = models.CharField(max_length=50, choices=PARTICIPACION)
    indexado = models.BooleanField(default=False)
    arbitrado = models.BooleanField(default=False)
    literatura_gris = models.BooleanField(default=False)


class Resultado(ElementoCientifico):
    NIVEL = (
        ('1', 'Primer Nivel'),
        ('2', 'Segundo Nivel'),
        ('3', 'Tercer Nivel'),
    )

    aprobado_cc = models.BooleanField(default=False)
    premios = models.ManyToManyField(Premio, null=True, blank=True)
    nivel = models.CharField(max_length=40, choices=NIVEL
                             )


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
    fecha_inicio = models.DateField(default=datetime.datetime.now())
    fecha_terminacion = models.DateField()
    entidadejecutora = models.ForeignKey(Entidad, on_delete=models.DO_NOTHING, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    resultados = models.ManyToManyField(Resultado, null=True, blank=True)
    entidades = models.ManyToManyField(Entidad, related_name="entidades_participantes", null=True, blank=True)


class Libro(models.Model):
    isbn = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
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

    def __str__(self):
        return self.titulo


class Servicio(models.Model):
    TIPO = (
        ('Estatal', 'Estatal'),
        ('Comercial', 'Comercial'),
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    fecha_inicio = models.DateField()
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

    def __str__(self):
        return self.nombre
