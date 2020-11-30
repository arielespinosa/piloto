import django
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from .nomencladores import (
    Especialidad, Premio, Plaza, Oficina, OrganismoMasas, OrganismoPolitico, Tarea
)



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


class AreaInteres(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    SEXO = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),)

    GRADO_CIENTIFICO = (
        ('MSc', 'Master en Ciencias'),
        ('Dr', 'Doctor en Ciencias'),)

    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    sexo = models.CharField(max_length=20, choices=SEXO)
    grado_cientifico = models.CharField(max_length=50, choices=GRADO_CIENTIFICO, null=True, blank=True)

    def __str__(self):
        return self.nombre +' '+ self.apellido1 +' '+ self.apellido2

    @property
    def nombre_completo(self):     
        return self.nombre +' '+ self.apellido1 +' '+ self.apellido2


class PersonaExterna(Persona):
    pass


class Trabajador(Persona):
    CATEGORIA_OCUPACIONAL= (
        ('T', 'Técnico'),
        ('E', 'Especialista'),
    )

    TIPO_PLANTILLA = (
        ('AP', 'A prueba'),
        ('F', 'Fijo'),)

    RAZA = (
        ('B', 'Blanca'),
        ('M', 'Mestiza'),
        ('N', 'Negra'),)

    NIVEL_ESCOLAR = (
        ('M', 'Medio'),
        ('S', 'Superior'),)


    CATEGORIA_CIENTIFICA = (
        ('AI', 'Aspirante a Investigador'),
        ('IA', 'Investigador Agregado'),
        ('IT', 'Investigador Titular'),)

    CATEGORIA_DOCENTE = (
        ('PI', 'Profesor Instructor'),
        ('PS', 'Profesor Asistente'),
        ('PX', 'Profesor Auxiliar'),
        ('PA', 'Profesor Agregado'),
        ('PT', 'Profesor Titular'),
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_de_perfiles/', default='avatar_default.jpg', null=True)
    ci = models.CharField(max_length=11)
    raza = models.CharField(max_length=20, choices=RAZA)

    nivel_escolar = models.CharField(max_length=50, choices=NIVEL_ESCOLAR)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING)
   
    cateogoria_cientifica = models.CharField(max_length=50, choices=CATEGORIA_CIENTIFICA, null=True, blank=True)
    cateogoria_docente = models.CharField(max_length=50, choices=CATEGORIA_DOCENTE, null=True, blank=True)
    
    tarjeta = models.IntegerField(unique=True)
    plaza = models.ForeignKey(Plaza, on_delete=models.DO_NOTHING)
    oficina = models.ForeignKey(Oficina, on_delete=models.DO_NOTHING)
    categoria_ocupacional = models.CharField(max_length=20, choices=CATEGORIA_OCUPACIONAL)
    fecha_entrada_insmet = models.DateField(default=django.utils.timezone.now)
    fecha_salida = models.DateField(null=True, blank=True)
    motivos_salida = models.TextField(max_length=1000, blank=True, null=True)

    res_34_19 = models.FloatField(blank=True, null=True)
    msc_dr = models.FloatField(blank=True, null=True)  # Lo que cobra por ser mst o phd
    otros_pagos_antiguo = models.FloatField(blank=True, null=True)
    otros_pagos_actual = models.FloatField(blank=True, null=True)
 
    direccion = models.CharField(max_length=200, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    membresias = models.ManyToManyField(OrganismoPolitico, null=True, blank=True)
    afiliaciones = models.ManyToManyField(OrganismoMasas, null=True, blank=True)

    areas_de_interes = models.ManyToManyField(AreaInteres, null=True, blank=True)
    contacto = models.ManyToManyField(Contacto, null=True, blank=True)


    def __str__(self):
        return self.nombre_coloquial

    @property
    def nombre_coloquial(self):
        if self.grado_cientifico:
            return self.grado_cientifico +'. '+ self.nombre +' '+ self.apellido1 +' '+ self.apellido2
        elif self.especialidad:
            return self.especialidad.categoria +'. '+ self.nombre +' '+ self.apellido1 +' '+ self.apellido2
        else:
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



class PremioTrabajador(models.Model):
    fecha = models.DateField()
    premio = models.ForeignKey(Premio, on_delete=models.DO_NOTHING)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.premio


class TareaTrabajador(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.DO_NOTHING)
    trabajadores = models.ManyToManyField(Trabajador)

    def __str__(self):
        return self.tarea.nombre

