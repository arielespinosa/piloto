from django.db import models
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


class GrupoTrabajo(models.Model):
    nombre = models.CharField(max_length=10)
    #responsable = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class CentroCosto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


