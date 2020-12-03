from django.urls import path
from .views import trabajo_cientifico as v_trabajo_cientifico
from .views import trabajador as v_trabajador
from .views import docencia as v_docencia
from .views import nomencladores as v_nomencladores

from django_pdfkit import PDFView


app_name = 'trabajador'

urlpatterns = [
    path('', v_trabajador.PerfilTrabajador.as_view(), name='perfil'),
    path('crear/persona_externa/', v_trabajador.CrearPersonaExterna.as_view(), name="crear_persona_externa"),
    path('modificar/<int:pk>', v_trabajador.ModificarTrabajador.as_view(), name='modificar_datos_personales'),
    
    path('cv/', v_trabajador.TrabajadorCV.as_view(), name='exportar_cv'),

    # NOMENCLADORES ----------
    # Crear
    path('crear/premio/', v_nomencladores.CrearPremio.as_view(), name='crear_premio'),
    path('crear/certificacion/', v_nomencladores.CrearCertificacion.as_view(), name="crear_certificacion"),
    path('crear/especialidad/', v_nomencladores.CrearEspecialidad.as_view(), name='crear_especialidad'),
    path('crear/entidad/', v_nomencladores.CrearEntidad.as_view(), name='crear_entidad'),
    path('crear/programa/', v_nomencladores.CrearPrograma.as_view(), name='crear_programa'),
    path('crear/cliente/', v_nomencladores.CrearCliente.as_view(), name='crear_cliente'),
    path('crear/centro_de_costo/', v_nomencladores.CrearCentroCosto.as_view(), name='crear_centro_de_costo'),
    path('crear/centro_de_estudios/', v_nomencladores.CrearCentroEstudios.as_view(), name="crear_centro_de_estudios"),
    path('centros_de_estudios/', v_nomencladores.ListaCentrosEstudios.as_view(), name="centros_de_estudios"),
    path('ver/centros_de_estudios/<int:pk>', v_nomencladores.VerCentroEstudios.as_view(), name="ver_centro_de_estudios"),
    path('eliminar/centros_de_estudios/<int:pk>', v_nomencladores.EliminarCentroEstudios.as_view(), name="eliminar_centro_de_estudios"),

    # TRABAJO CIENTIFICO -------------
    # Crear
    path('crear/tesis/', v_trabajo_cientifico.CrearTesis.as_view(), name="crear_tesis"),
    path('ver/tesis/<int:pk>', v_trabajo_cientifico.VerTesis.as_view(), name="ver_tesis"),
    path('eliminar/tesis/<int:pk>', v_trabajo_cientifico.EliminarTesis.as_view(), name="eliminar_tesis"),


    path('crear/proyecto/', v_trabajo_cientifico.CrearProyecto.as_view(), name='crear_proyecto'),
    path('crear/articulo/', v_trabajo_cientifico.CrearArticulo.as_view(), name='crear_articulo'),
    path('crear/libro/', v_trabajo_cientifico.CrearLibro.as_view(), name='crear_libro'),
    path('crear/resultado/', v_trabajo_cientifico.CrearResultado.as_view(), name='crear_resultado'),
    path('crear/servicio/', v_trabajo_cientifico.CrearServicio.as_view(), name='crear_servicio'),
    path('crear/premio_cientifico/', v_trabajo_cientifico.CrearPremioElementoCientifico.as_view(), name='crear_premio_cientifico'),
        
    # Ver
    path('ver/proyecto/<int:pk>', v_trabajo_cientifico.VerProyecto.as_view(), name='ver_proyecto'),
    path('ver/articulo/<int:pk>', v_trabajo_cientifico.VerArticulo.as_view(), name='ver_articulo'),
    path('ver/libro/<int:pk>', v_trabajo_cientifico.VerLibro.as_view(), name='ver_libro'),
    path('ver/resultado/<int:pk>', v_trabajo_cientifico.VerResultado.as_view(), name='ver_resultado'),
    path('ver/servicio/<int:pk>', v_trabajo_cientifico.VerServicio.as_view(), name='ver_servicio'),

    # Eliminar
    path('eliminar/proyecto/<int:pk>', v_trabajo_cientifico.EliminarProyecto.as_view(), name='eliminar_proyecto'),
    path('eliminar/articulo/<int:pk>', v_trabajo_cientifico.EliminarArticulo.as_view(), name='eliminar_articulo'),
    path('eliminar/libro/<int:pk>', v_trabajo_cientifico.EliminarLibro.as_view(), name='eliminar_libro'),
    path('eliminar/resultado/<int:pk>', v_trabajo_cientifico.EliminarResultado.as_view(), name='eliminar_resultado'),
    path('eliminar/servicio/<int:pk>', v_trabajo_cientifico.EliminarServicio.as_view(), name='eliminar_servicio'),

    # DOCENCIA
    # Crear
    path('crear/evento/', v_docencia.CrearEvento.as_view(), name="crear_evento"),
    path('crear/certificacion_trabajador/', v_docencia.CrearCertificarTrabajador.as_view(), name="crear_certificacion_trabajador"),
    path('crear/curso/', v_docencia.CrearCurso.as_view(), name="crear_curso"),
    path('crear/curso_realizado/', v_docencia.CrearCursoRealizado.as_view(), name="crear_curso_realizado"),
    path('crear/ponencia/', v_docencia.CrearPonencia.as_view(), name="crear_ponencia"),
    path('crear/oponencia/',v_docencia.CrearOponencia.as_view(), name="crear_oponencia"),    
    path('crear/tribunal/', v_docencia.CrearTribunal.as_view(), name="crear_tribunal"),
    path('crear/tutoria/', v_docencia.CrearTutoria.as_view(), name="crear_tutoria"),
 
    # Listar
    path('eventos/', v_docencia.ListaEventos.as_view(), name="eventos"),
    path('ponencias/', v_docencia.ListaPonencias.as_view(), name="ponencias"),
    path('oponencias/', v_docencia.ListaOponencias.as_view(), name="oponencias"),
    path('tribunal/', v_docencia.ListaTribunales.as_view(), name="tribunal"),

    # Ver
    path('ver/evento/<int:pk>', v_docencia.VerEvento.as_view(), name="ver_evento"),
    path('ver/ponencia/<int:pk>', v_docencia.VerPonencia.as_view(), name="ver_ponencia"),
    path('ver/oponencia/<int:pk>', v_docencia.VerOponencia.as_view(), name="ver_oponencia"),
    path('ver/tribunal/<int:pk>', v_docencia.VerTribunal.as_view(), name="ver_tribunal"),
 
    # Modificar
    path('eventos/modificar/<int:pk>', v_docencia.ModificarEvento.as_view(), name="modificar_evento"),

    # Eliminar
    path('eliminar/evento/<int:pk>', v_docencia.EliminarEvento.as_view(), name='eliminar_evento'),
    path('eliminar/ponencia/<int:pk>', v_docencia.EliminarPonencia.as_view(), name="eliminar_ponencia"),
    path('eliminar/oponencia/<int:pk>', v_docencia.EliminarOponencia.as_view(), name="eliminar_oponencia"),
    path('eliminar/tribunal/<int:pk>', v_docencia.EliminarTribunal.as_view(), name="eliminar_tribunal"),
    path('eliminar/tutoria/<int:pk>', v_docencia.EliminarTutoria.as_view(), name="eliminar_tutoria"),
 
 

]