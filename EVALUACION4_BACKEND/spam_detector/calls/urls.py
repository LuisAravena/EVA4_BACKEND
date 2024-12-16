from rest_framework.routers import DefaultRouter
from .views import (
    NumeroViewSet, ReporteViewSet, UsuarioViewSet, exportar_csv, 
    numero_list, numero_create, numero_update, numero_delete
)
from django.urls import path, include

# Configuración del router
router = DefaultRouter()
router.register(r'api/numeros', NumeroViewSet)
router.register(r'api/reportes', ReporteViewSet)
router.register(r'api/usuarios', UsuarioViewSet)

# Definición de las rutas
urlpatterns = [
    # Rutas para vistas basadas en funciones
    path('numeros/', numero_list, name='numero_list'),
    path('numeros/nuevo/', numero_create, name='numero_create'),
    path('numeros/<int:pk>/editar/', numero_update, name='numero_update'),
    path('numeros/<int:pk>/eliminar/', numero_delete, name='numero_delete'),
    path('exportar-csv/', exportar_csv, name='exportar_csv'),
    
    # Rutas del router
    path('', include(router.urls)),  # Incluye las rutas del router
]
