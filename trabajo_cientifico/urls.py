from django.urls import path
from . import views

app_name = 'trabajo_cientifico'

urlpatterns = [
    path('',  views.inicio, name='inicio'),
    path('crear_proyecto/', views.CrearProyecto.as_view(), name='crear_proyecto'),
    path('crear_articulo/', views.CrearArticulo.as_view(), name='crear_articulo'),
    path('crear_libro/', views.CrearLibro.as_view(), name='crear_libro'),
    path('crear_literatura_gris/', views.CrearLiteraturaGris.as_view(), name='crear_literatura_gris'),
    path('crear_resultado/', views.CrearResultado.as_view(), name='crear_resultado'),
    path('crear_servicio/', views.CrearServicio.as_view(), name='crear_servicio'),

]