from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from trabajo_cientifico.models import (
    Articulo, Libro, LiteraturaGris, Proyecto, Resultado, Servicio
)
from docencia.models import (
    Oponencia, Evento, Certificacion, Ponencia, Tesis, Tribunal
)

# from centro.models import Local


class Plaza(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    TIPO_DE_CONTACTO = (
        ('T', 'Telefono'),
        ('M', 'Movil'),
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
    valor = models.CharField(max_length=50, choices=DESCRIPCION)

    def __str__(self):
        return self.valor


class Municipio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Afiliacion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class AreasInteres(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=500, null=True, blank=True)
    apellido1 = models.CharField(max_length=50, null=True, blank=True)
    apellido2 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Trabajador(Persona):

    CATEGORIA_OCUPACIONAL= (
        ('T', 'T'),
        ('E', 'E'),
    )

    ESPECIALIDAD = (
        ('T', 'T'),
        ('E', 'E'),
    )

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

    TIPO_PLANTILLA = (
        ('F', 'F'),)

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
    ci = models.CharField(max_length=11, null=True, blank=True)
    sexo = models.CharField(max_length=20, choices=SEXO, null=True, blank=True)
    raza = models.CharField(max_length=20, choices=RAZA, null=True, blank=True)
    nivel_escolar = models.CharField(max_length=50, choices=NIVEL_ESCOLAR, null=True, blank=True)
    especialidad = models.CharField(max_length=50, choices=ESPECIALIDAD, null=True, blank=True)
    grado_cientifico = models.CharField(max_length=50, choices=GRADO_CIENTIFICO, null=True, blank=True)
    cateogoria_cientifica = models.CharField(max_length=50, choices=CATEGORIA_CIENTIFICA, blank=True)
    cateogoria_docente = models.CharField(max_length=50, choices=CATEGORIA_DOCENTE, null=True, blank=True)
    
    tarjeta = models.IntegerField()
    categoria_ocupacional = models.CharField(max_length=40, choices=CATEGORIA_OCUPACIONAL, null=True, blank=True)
    fecha_entrada_insmet = models.DateField(null=True, blank=True)
    fecha_salida = models.DateField(blank=True, null=True)
    motivos_salida = models.TextField(max_length=1000, blank=True)
    res_34_19 = models.FloatField(blank=True, null=True)
    msc_dr = models.FloatField(blank=True, null=True)  # Lo que cobra por ser mst o phd
    grupo_escala_antiguo = models.CharField(max_length=5, choices=GRUPO_ESCALA, blank=True, null=True)
    grupo_escala_actual = models.CharField(max_length=5, choices=GRUPO_ESCALA, null=True, blank=True)
    salario_escala_antiguo = models.FloatField(blank=True, null=True)
    salario_escala_actual = models.FloatField(default=0, blank=True, null=True)
    otros_pagos_antiguo = models.FloatField(blank=True, null=True)
    otros_pagos_actual = models.FloatField(blank=True, null=True)
    salario_total_antiguo = models.FloatField(blank=True, null=True)
    salario_total_actual = models.FloatField(default=0, blank=True, null=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    #membresias = models.ForeignKey(Organismos, on_delete=models.DO_NOTHING null=True, blank=True) # que es esto?
    
    municipio = models.ForeignKey(Municipio, on_delete=models.DO_NOTHING, null=True, blank=True)
    #oficina = models.ForeignKey(Oficina, on_delete=models.DO_NOTHING, null=True, blank=True)
    plaza = models.ForeignKey(Plaza, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    areas_de_interes = models.ManyToManyField(AreasInteres, blank=True, null=True)
    contacto = models.ManyToManyField(Contacto, blank=True, null=True)
    proyectos = models.ManyToManyField(Proyecto, blank=True, null=True)
    afiliaciones = models.ManyToManyField(Afiliacion, blank=True, null=True)
    servicios = models.ManyToManyField(Servicio, blank=True, null=True)
    libros = models.ManyToManyField(Libro, blank=True, null=True)
    articulos = models.ManyToManyField(Articulo, blank=True, null=True)
    literatura_gris = models.ManyToManyField(LiteraturaGris, blank=True, null=True)
    certificaciones = models.ManyToManyField(Certificacion, blank=True, null=True)
    ponencias = models.ManyToManyField(Ponencia, blank=True, null=True)
    oponencias = models.ManyToManyField(Oponencia, blank=True, null=True)
    tesis = models.ManyToManyField(Tesis, blank=True, null=True)
    tribunales = models.ManyToManyField(Tribunal, blank=True, null=True)
    eventos = models.ManyToManyField(Evento, blank=True, null=True)
    resultados = models.ManyToManyField(Resultado, blank=True, null=True)

    @property
    def nombre_coloquial(self):

        if self.grado_cientifico:
            return self.grado_cientifico +' '+ self.nombre +' '+ self.apellido1 +' '+ self.apellido2
        else:
            return self.nombre +' '+ self.apellido1 +' '+ self.apellido2

    @property
    def fecha_nacimiento(self):
        return datetime(1991, 11, 28)
    
    @property
    def diferencia_salarial(self):
        return self.salario_escala_actual - self.salario_escala_antiguo

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("recursos_humanos:perfil_trabajador", kwargs={"id":self.id})
