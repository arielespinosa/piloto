from django.db import models

NIVEL = (
    ('N', 'Nacional'),
    ('I', 'Internacional'),
)

class CentroEstudios(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=500)
    fecha = models.DateField()
    lugar = models.CharField(max_length=250)
    nivel = models.CharField(max_length=20, choices=NIVEL)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Certificacion(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_profesor = models.CharField(max_length=100)
    cantidad_horas = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    centro_estudios = models.ForeignKey(CentroEstudios, on_delete=models.DO_NOTHING)
    creditos = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

# Oponencia y tribunal tienen los mismos campos ??? Una oponencia tiene un tribunal...y un tribunal esta
# compuesto por muchas personas
class Oponencia(models.Model):
    TIPO = (
        ('Articulo', 'Articulo'),
        ('Tesis', 'Tesis'),
        ('Proyecto', 'Proyecto'),
        ('Resultados', 'Resultados'),
    )

    titulo = models.CharField(max_length=100)
    autor_principal = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo

class Tribunal(models.Model):
    titulo = models.CharField(max_length=100)
    autor_principal = models.CharField(max_length=100)
    #tipo = models.CharField(max_length=20, choices=TIPO_OPONENCIA)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo

class Tesis(models.Model):
    GRADO_ESCOLAR = (
        ('S', 'Superior'),
        ('MSc', 'Master'),
        ('PhD', 'Doctorado'),
    )

    grado = models.CharField(max_length=3, choices=GRADO_ESCOLAR)
    especialidad = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100) # el autor no se refiere a un trabajador del centro?
    lugar = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo


class Ponencia(models.Model):
    PARTICIPACION = (
        ('API_CO','Autor Principal Invitado por CO'),
        ('PAP', 'Ponente Autor Principal'),
        ('P', 'Ponente'),
    )

    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING) # añadi esto..me parec que una ponencia se hace en un evento
    titulo = models.CharField(max_length=100)
    participacion = models.CharField(max_length=40, choices=PARTICIPACION)
    autores = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo



# No entiendo la relacion entre Ponencia, Evento, Trabajador...linea 561-575