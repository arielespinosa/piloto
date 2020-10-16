from django.urls import path
from . import views

app_name = 'trabajador'

urlpatterns = [
    path('', views.PerfilTrabajador.as_view(), name='perfil'),
    #path('trabajador/<int:pk>/actualizar', views.AppUserUpdateView.as_view(), name='update_appuser'),


]