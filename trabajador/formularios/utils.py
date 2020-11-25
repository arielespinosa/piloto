from trabajador.modelos.trabajadores import Trabajador, PersonaExterna

def trabajadores_personas_choices(exclude_trabajador=False):
    if exclude_trabajador:      
        choices = [(t.pk, '{0} {1} {2}'.format(t.nombre, t.apellido1, t.apellido2)) for t in Trabajador.objects.all().exclude(pk=self.request.user.trabajador.pk)]       
    else:
        choices = [(t.pk, '{0} {1} {2}'.format(t.nombre, t.apellido1, t.apellido2)) for t in Trabajador.objects.all()]       
    choices += [(p.pk, '{0} {1} {2}'.format(p.nombre, p.apellido1, p.apellido2)) for p in PersonaExterna.objects.all()]
    
    return choices

