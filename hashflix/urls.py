from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('filme.urls', namespace='filme')),
]

# Usar as imagens estaticas (abrir em uma nova guia do navegador)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Fazer upload das imagens
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
