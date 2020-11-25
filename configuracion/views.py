from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic import DetailView
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LoginView
from . import forms
from trabajador.modelos.trabajadores import Trabajador
from .mixins import AjaxFormMixin, BSModalAjaxFormMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

import time

from django.contrib.auth.decorators import login_required


# -----------------------------------------
class IniciarSesion(LoginView):
    template_name = 'login.html'
    authentication_form = forms.FormAutenticacion

# -----------------------------------------
class RegistrarTrabajador(CreateView):
    template_name  = 'registrar_trabajador.html'
    form_class = forms.FormRegistrarTrabajador
    form_registrar_usuario = forms.FormRegistrarUsuario    
    success_message = 'Su cuenta se creó satisfactoriamente.'
    success_url = reverse_lazy('configuracion:login')

    def get_context_data(self, **kwargs):
        context = super(RegistrarTrabajador, self).get_context_data(**kwargs)
        context['form'] =  self.get_form(self.form_class)
        context['form_usuario'] = self.get_form(self.form_registrar_usuario)
        return context

    def post(self, request, *args, **kwargs):
        form_registrar_usuario = self.form_registrar_usuario(request.POST)
        form_registrar_trabajador = self.form_class(request.POST)

        if form_registrar_usuario.is_valid() and form_registrar_trabajador.is_valid():
            trabajador = form_registrar_trabajador.save(commit=False)
            usuario = form_registrar_usuario.save(commit=False)

            usuario.is_active = False
            usuario.save()
            trabajador.usuario = usuario
            trabajador.save()

            return HttpResponseRedirect('/')
        else:
            return render(request, self.template_name, {
                'form': form_registrar_trabajador,
                'form_usuario': form_registrar_usuario,
            })


class AppUserProfile(DetailView):
    template_name = "user_profile.html"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Trabajador, id=id)

# -----------------------------------------
class AppUserUpdateView(BSModalAjaxFormMixin, BSModalUpdateView):
    model = Trabajador
    template_name = 'additional/update_appuser.html'
    form_class = forms.FormAppUser
    success_message = 'Su información personal fue modificada satisfactoriamente.'
    #success_url = reverse_lazy('forecast')







