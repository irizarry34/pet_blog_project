from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Configuración de la vista de esquema para Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Pet Blog API",
        default_version='v1',
        description="API para un blog sobre mascotas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@petblogapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración de Django
    path('api/', include('blogapp.urls')),  # Incluye las rutas de la aplicación 'blogapp'
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
