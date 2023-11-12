from django.shortcuts import render
# IMPORTACIONES DE REST
from rest_framework.viewsets import ModelViewSet

# IMPORTACIONES DE SERIALIZERS
from .serializers import BookLocationSerializer, SectionSerializer, ShelfSerializer
from rest_framework.permissions import BasePermission

# IMPORTACIONES DE LOS MODULOS
from .models import BookLocation, Shelf, Section

# Permisos
class CatalogadorOrAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.rol in [2, 4]   # Verifica si el usuario tiene el rol de Catalogador o Administrador
    
    def has_object_permission(self, request, view, obj):
        if request.method in ['POST', 'PUT', 'PATCH'] and request.user.rol == 4:    # Permite la creación y actualización si el usuario es Administrador
            return True
        elif request.method in ['PUT', 'PATCH'] and request.user.rol == 2:          # Permite la actualización solo si el usuario es Catalogador
            return True
        return False                                                                 # Deniega el resto de los métodos

# Create your views here.
class BookLocationViewSet(ModelViewSet):            # VISTA DE LAS UBICACIONES
    serializer_class = BookLocationSerializer
    queryset = BookLocation.objects.all()
    permission_classes = [CatalogadorOrAdminPermission]

class SectionViewSet(ModelViewSet):            # VISTA DE LAS SECCIONES
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [CatalogadorOrAdminPermission]

class ShelfViewSet(ModelViewSet):            # VISTA DE LOS ESTANTES
    serializer_class = ShelfSerializer
    queryset = Shelf.objects.all()
    permission_classes = [CatalogadorOrAdminPermission]
