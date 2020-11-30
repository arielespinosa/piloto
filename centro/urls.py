from django.urls import path
from .views import centro as v_centro
from .views import reportes as v_reportes


app_name = 'centro'

urlpatterns = [
    path('',  v_centro.Inicio.as_view(), name='inicio'),
    path('plan_de_trabajo/',  v_centro.plan_de_trabajo, name='plan_de_trabajo'),
    
    # Reportes
    path('reportes/balance/', v_reportes.BalanceAnual.as_view(), name='reporte_balance_anual'),
    # Objeto ----------------------------------------------------------------
    path('crear/objeto/', v_centro.CrearObjeto.as_view(), name='crear_objeto'),
    path('actualizar/objeto/<int:pk>', v_centro.ActualizarObjeto.as_view(), name='actualizar_objeto'),
    path('objeto/', v_centro.ListaObjeto.as_view(), name='objetos'),
    path('ver/objeto/<int:pk>', v_centro.DetalleObjeto.as_view(), name='ver_objeto'),
    path('eliminar/objeto/<int:pk>', v_centro.EliminarObjeto.as_view(), name='eliminar_objeto'),

    # Local ----------------------------------------------------------------
    path('crear/local/', v_centro.CrearLocal.as_view(), name='crear_local'),
    path('actualizar/local/<int:pk>', v_centro.ActualizarInventario.as_view(), name='actualizar_local'),
    path('local/', v_centro.ListaInventario.as_view(), name='locales'),
    path('ver/local/<int:pk>', v_centro.DetalleInventario.as_view(), name='ver_local'),
    path('eliminar/local/<int:pk>', v_centro.EliminarInventario.as_view(), name='eliminar_local'),
    
    # Inventario ----------------------------------------------------------------
    path('crear/inventario/', v_centro.CrearInventario.as_view(), name='crear_inventario'),
    path('actualizar/inventario/<int:pk>', v_centro.ActualizarInventario.as_view(), name='actualizar_inventario'),
    path('inventario/', v_centro.ListaInventario.as_view(), name='inventario'),
    path('ver/inventario/<int:pk>', v_centro.DetalleInventario.as_view(), name='ver_inventario'),
    path('eliminar/inventario/<int:pk>', v_centro.EliminarInventario.as_view(), name='eliminar_inventario'),
]