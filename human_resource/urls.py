from django.urls import path
from . import views

app_name = 'recursos_humanos'

urlpatterns = [
    path('',  views.inicio, name='inicio'),    
    path('trabajador/<int:id>', views.PerfilTrabajador.as_view(), name='perfil_trabajador'),
    #path('trabajador/<int:pk>/actualizar', views.AppUserUpdateView.as_view(), name='update_appuser'),


]