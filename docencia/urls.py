from django.urls import path
from . import views

app_name = 'docencia'

urlpatterns = [
    path('',  views.inicio, name='inicio'),
    path('tesis/', views.ListaTesis.as_view(), name="tesis"),
    path('crear_evento/', views.CrearEvento.as_view(), name="crear_evento"),
    path('ver_evento/<int:pk>', views.VerEvento.as_view(), name="ver_evento"),
    path('eliminar_evento/<int:pk>', views.EliminarEvento.as_view(), name='eliminar_evento'),
    path('crear_tesis/', views.CrearTesis.as_view(), name="crear_tesis"),
    path('crear_ponencia/', views.CrearPonencia.as_view(), name="crear_ponencia"),
    path('crear_oponencia/', views.CrearOponencia.as_view(), name="crear_oponencia"),    
    path('crear_tribunal/', views.CrearTribunal.as_view(), name="crear_tribunal"),
    path('crear_certificacion/', views.CrearCertificacion.as_view(), name="crear_certificacion"),
    path('certificaciones/', views.ListaCertificaciones.as_view(), name="certificaciones"),
    path('ponencias/', views.ListaPonencias.as_view(), name="ponencias"),

]