from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from gm2m import GM2MField
from django.db import models
from centro.modelos.nomencladores import Lugar
from .trabajadores import Trabajador, PersonaExterna
from .nomencladores import CampoEspecialidad, CentroEstudios
from .trabajo_cientifico import Resultado, Tesis


class Certificacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    cantidad_horas = models.FloatField()
    centro_estudios = models.ForeignKey(CentroEstudios, on_delete=models.DO_NOTHING)
    creditos = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)
    certificacion = models.ForeignKey(Certificacion, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo


class CursoRealizado(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    edicion = models.PositiveSmallIntegerField()
    profesor = GenericForeignKey('content_type', 'object_id')
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    estudiantes = models.ManyToManyField(Trabajador, related_name='cursos_recibidos')

    def __str__(self):
        return self.curso.titulo


# Ok
class Evento(models.Model):
    NIVEL = (
        ('N', 'Nacional'),
        ('I', 'Internacional'),
    )

    fecha = models.DateField()
    nombre = models.CharField(max_length=500)    
    lugar = models.ForeignKey(Lugar, on_delete=models.DO_NOTHING)
    nivel = models.CharField(max_length=20, choices=NIVEL)
    descripcion = models.TextField(null=True, blank=True)
    participantes = models.ManyToManyField(Trabajador, null=True, blank=True)

    def __str__(self):
        return self.nombre


# Ok
class Oponencia(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    fecha = models.DateField()
    
    # Puede ser: Articulo, Tesis, Resultado, Proyecto
    elemento = GenericForeignKey('content_type', 'object_id')
    
    # Puede ser: Trabajador o PersonaExterna
    oponentes = GM2MField(Trabajador, PersonaExterna, related_name='oponencias')

    def __str__(self):
        return self.elemento.titulo


# Ok
class Ponencia(models.Model):
    titulo = models.CharField(max_length=100)    
    autores = GM2MField(Trabajador, PersonaExterna, related_name='ponencias')

    def __str__(self):
        return self.titulo


# Ok
class PonenciasRealizadas(models.Model):   
    PARTICIPACION = (
        ('API_CO','Autor Principal Invitado por CO'),
        ('PAP', 'Ponente Autor Principal'),
        ('P', 'Ponente'),
    ) 
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING)
    ponencia = models.ForeignKey(Ponencia, on_delete=models.DO_NOTHING)
    participacion = models.CharField(max_length=40, choices=PARTICIPACION)
    ponente = models.ForeignKey(Trabajador, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ponencia.titulo


# Ok
class Tribunal(models.Model):
    fecha = models.DateField()
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE)
    miembros = GM2MField(Trabajador, PersonaExterna, related_name='tribunales')

    def __str__(self):
        return self.tesis.titulo
 

# Ok
class Comision(models.Model):
    fecha = models.DateField()
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE)
    integrantes = GM2MField(Trabajador, PersonaExterna, related_name='comisiones')

    def __str__(self):
        return self.resultado.titulo


# Eliminar esto
class Tutoria(models.Model):
    fecha_inicio = models.DateField()
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='tutorias')

    def __str__(self):
        return self.tesis.titulo

    @property
    def fecha_culminacion(self):
        self.tesis.fecha_culminacion
