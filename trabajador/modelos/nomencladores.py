from datetime import datetime
from django.db import models
from gm2m import GM2MField


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class CentroCosto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class CentroEstudios(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# Meteorologia, Informática, Cibernetica, Fisica
class CampoEspecialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Especialidad(models.Model):
    CATEGORIAS = (
        ('Téc', 'Técnico'),
        ('Ing', 'Ingeniero'),
        ('Lic', 'Licenciado'),
    )

    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    campo = models.ForeignKey(CampoEspecialidad, on_delete=models.DO_NOTHING)
    centro_de_estudio = models.ForeignKey(CentroEstudios, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.categoria


class Plaza(models.Model):
    GRUPO_ESCALA = (
    ('V', 'V'),
    ('VI', 'VI'),
    ('VII', 'VII'),
    ('VIII', 'VIII'),
    ('IX', 'IX'),
    ('X', 'X'),
    ('XI', 'XI'),
    ('XII', 'XII'),
    ('XIII', 'XIII'),
    ('XIV', 'XIV'),
    ('XV', 'XV'),
    ('XVI', 'XVI'),
    ('XVII', 'XVII'),
    ('XVIII', 'XVIII'),
    ('XIX', 'XIX'),
    ('XX', 'XX'),
    ('XXI', 'XXI'),
    ('XXII', 'XXII'),
    ('XXIII', 'XXIII'),
    ('XXIV', 'XXIV'),
    ('XXV', 'XXV'),)

    nombre = models.CharField(max_length=100, unique=True)
    grupo_escala_antiguo = models.CharField(max_length=10, choices=GRUPO_ESCALA, blank=True, null=True)
    grupo_escala_actual = models.CharField(max_length=10, choices=GRUPO_ESCALA)
    salario_escala_antiguo = models.FloatField(blank=True, null=True)
    salario_escala_actual = models.FloatField()

    def __str__(self):
        return self.nombre


class Oficina(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class OrganismoMasas(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class OrganismoPolitico(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre



class Premio(models.Model):
    NIVEL = (
        ('CITMA', 'Ministerio de Ciencia, Tecnología y Medio Ambiente'),
        ('ACC', 'Academia de Ciencias'),
        ('MES', 'Ministerio de Educación Superior'),
        ('O', 'Otro'),
    )

    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50, choices=NIVEL, null=True, blank=True)
  
    def __str__(self):
        return self.nombre


class Entidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Programa(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



