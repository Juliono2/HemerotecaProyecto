from django.shortcuts import render
# IMPORTACIONES DE REST
from rest_framework.viewsets import ModelViewSet

# IMPORTACIONES DE SERIALIZERS
from .serializers import BookLocationSerializer, SectionSerializer, ShelfSerializer
from rest_framework.permissions import BasePermission

# IMPORTACIONES DE LOS MODULOS
from .models import BookLocation, Shelf, Section

# Permisos
class ViewPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class CatalogadorOrAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST']:                   # Permite la creación si el usuario es Administrador
            return request.user.rol == 4
        elif request.method in ['PUT', 'PATCH']:         # Permite la actualización solo si el usuario es Catalogador o admin
            return request.user.rol in  [2,4]
        return True                                      # Deniega el resto de los métodos

# Create your views here.
class BookLocationViewSet(ModelViewSet):            # VISTA DE LAS UBICACIONES
    serializer_class = BookLocationSerializer
    queryset = BookLocation.objects.all()
    permission_classes = [CatalogadorOrAdminPermission, ViewPermission]

class SectionViewSet(ModelViewSet):            # VISTA DE LAS SECCIONES
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [CatalogadorOrAdminPermission, ViewPermission]

class ShelfViewSet(ModelViewSet):            # VISTA DE LOS ESTANTES
    serializer_class = ShelfSerializer
    queryset = Shelf.objects.all()
    permission_classes = [CatalogadorOrAdminPermission, ViewPermission]
