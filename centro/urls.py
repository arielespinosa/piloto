from django.urls import path
from . import views

app_name = 'centro'

urlpatterns = [
    path('',  views.Inicio.as_view(), name='inicio'),
    path('plan_de_trabajo/',  views.plan_de_trabajo, name='plan_de_trabajo'),
    
    # Objeto ----------------------------------------------------------------
    path('crear/objeto/', views.CrearObjeto.as_view(), name='crear_objeto'),
    path('actualizar/objeto/<int:pk>', views.ActualizarObjeto.as_view(), name='actualizar_objeto'),
    path('objeto/', views.ListaObjeto.as_view(), name='objetos'),
    path('ver/objeto/<int:pk>', views.DetalleObjeto.as_view(), name='ver_objeto'),
    path('eliminar/objeto/<int:pk>', views.EliminarObjeto.as_view(), name='eliminar_objeto'),

    # Local ----------------------------------------------------------------
    path('crear/local/', views.CrearLocal.as_view(), name='crear_local'),
    path('actualizar/local/<int:pk>', views.ActualizarInventario.as_view(), name='actualizar_local'),
    path('local/', views.ListaInventario.as_view(), name='locales'),
    path('ver/local/<int:pk>', views.DetalleInventario.as_view(), name='ver_local'),
    path('eliminar/local/<int:pk>', views.EliminarInventario.as_view(), name='eliminar_local'),
    
    # Inventario ----------------------------------------------------------------
    path('crear/inventario/', views.CrearInventario.as_view(), name='crear_inventario'),
    path('actualizar/inventario/<int:pk>', views.ActualizarInventario.as_view(), name='actualizar_inventario'),
    path('inventario/', views.ListaInventario.as_view(), name='inventario'),
    path('ver/inventario/<int:pk>', views.DetalleInventario.as_view(), name='ver_inventario'),
    path('eliminar/inventario/<int:pk>', views.EliminarInventario.as_view(), name='eliminar_inventario'),
]