from trabajador.modelos.trabajadores import Trabajador, PersonaExterna
from trabajador.modelos.trabajo_cientifico import(
    Tesis, Articulo, Resultado, Proyecto, Libro, Servicio
)
from trabajador.modelos.docencia import CursoRealizado
from trabajador.modelos.nomencladores import Especialidad

def trabajadores_personas_choices(trabajador=None):
    if trabajador:      
        choices = [(t.pk, '{0} {1} {2}'.format(t.nombre, t.apellido1, t.apellido2)) for t in Trabajador.objects.all().exclude(pk=trabajador.pk)]       
    else:
        choices = [(t.pk, '{0} {1} {2}'.format(t.nombre, t.apellido1, t.apellido2)) for t in Trabajador.objects.all()]       
    choices += [(p.pk, '{0} {1} {2}'.format(p.nombre, p.apellido1, p.apellido2)) for p in PersonaExterna.objects.all()]
    return choices


def elementos_cientificos_choices():      
    choices = [(e.pk, '{0}: {1}'.format(type(e).__name__, e.titulo)) for e in Tesis.objects.all()]       
    choices += [(e.pk, '{0}: {1}'.format(type(e).__name__, e.titulo)) for e in Articulo.objects.all()]       
    choices += [(e.pk, '{0}: {1}'.format(type(e).__name__, e.titulo)) for e in Resultado.objects.all()]       
    choices += [(e.pk, '{0}: {1}'.format(type(e).__name__, e.titulo)) for e in Proyecto.objects.all()]       
    choices += [(e.pk, '{0}: {1}'.format(type(e).__name__, e.titulo)) for e in Libro.objects.all()] 
    return choices


def cursos_choices(trabajador=None):
    if trabajador:      
        choices = [(c.pk, 'Edición {0}: {1}'.format(c.edicion, c)) for c in CursoRealizado.objects.all()] # .exclude(estudiantes__pk=trabajador.pk)
    else:
        pass
    return choices


def especialidad_choices():
    choices = [(e.pk, '{0}. en {1}'.format(e.categoria, e.campo)) for e in Especialidad.objects.all()]
    return choices

