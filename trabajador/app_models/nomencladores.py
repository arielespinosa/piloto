from datetime import datetime
from django.db import models


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

    nombre = models.CharField(max_length=100)
    grupo_escala_antiguo = models.CharField(max_length=10, choices=GRUPO_ESCALA, blank=True, null=True)
    grupo_escala_actual = models.CharField(max_length=10, choices=GRUPO_ESCALA)
    salario_escala_antiguo = models.FloatField(blank=True, null=True)
    salario_escala_actual = models.FloatField()

    def __str__(self):
        return self.nombre


class Oficina(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    TIPO_DE_CONTACTO = (
        ('T', 'Teléfono'),
        ('M', 'Móvil'),
        ('E', 'Correo'),
        ('F', 'Fax'),    
    )

    DESCRIPCION = (
        ('P', 'Privado'),
        ('I', 'Institucional'),
        ('O', 'Otro'),  
    )

    tipo = models.CharField(max_length=20, choices=TIPO_DE_CONTACTO)
    descripcion = models.CharField(max_length=20, choices=DESCRIPCION)
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.valor


class Municipio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class OrganismoMasas(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class OrganismoPolitico(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class AreasInteres(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
