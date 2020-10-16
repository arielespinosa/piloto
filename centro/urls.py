from django.urls import path
from . import views

app_name = 'centro'

urlpatterns = [
    path('',  views.Inicio.as_view(), name='inicio'),
    path('plan_de_trabajo/',  views.plan_de_trabajo, name='plan_de_trabajo'),
    
    # Objeto ----------------------------------------------------------------
    path('objeto/add/', views.AddObjeto.as_view(), name='add_objeto'),
    path('objeto/actualizar/<int:pk>', views.ActualizarObjeto.as_view(), name='actualizar_objeto'),
    path('objeto/', views.ListaObjeto.as_view(), name='objetos'),
    path('objeto/ver/<int:pk>', views.DetalleObjeto.as_view(), name='ver_objeto'),
    path('objeto/eliminar/<int:pk>', views.EliminarObjeto.as_view(), name='eliminar_objeto'),
    # Local ----------------------------------------------------------------
    path('local/add/', views.AddInventario.as_view(), name='add_local'),
    path('local/actualizar/<int:pk>', views.ActualizarInventario.as_view(), name='actualizar_local'),
    path('local/', views.ListaInventario.as_view(), name='locales'),
    path('local/ver/<int:pk>', views.DetalleInventario.as_view(), name='ver_local'),
    path('local/eliminar/<int:pk>', views.EliminarInventario.as_view(), name='eliminar_local'),
    # Inventario ----------------------------------------------------------------
    path('inventario/add/', views.AddInventario.as_view(), name='add_inventario'),
    path('inventario/actualizar/<int:pk>', views.ActualizarInventario.as_view(), name='actualizar_inventario'),
    path('inventario/', views.ListaInventario.as_view(), name='inventario'),
    path('inventario/ver/<int:pk>', views.DetalleInventario.as_view(), name='ver_inventario'),
    path('inventario/eliminar/<int:pk>', views.EliminarInventario.as_view(), name='eliminar_inventario'),
]