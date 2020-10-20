from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', include(notifications.urls, namespace='notifications')),
    path('', include('configuracion.urls')),
    path('trabajador/', include('trabajador.urls')),
    path('centro/', include('centro.urls')),
    path('docencia/', include('docencia.urls')),
    path('trabajo_cientifico/', include('trabajo_cientifico.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)