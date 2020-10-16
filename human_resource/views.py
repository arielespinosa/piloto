from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Trabajador


def inicio(request):
    return render(request, 'recursos_humanos.html')

class PerfilTrabajador(DetailView):
    template_name = "perfil_de_trabajador.html"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Trabajador, id=id)

    