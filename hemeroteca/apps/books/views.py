from django.shortcuts import render

# IMPORTACIONES DE REST
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission

# IMPORTACIONES DE SERIALIZERS
from .serializers import BookSerializer, CopySerializer, PublicationSerializer

# IMPORTACIONES DE LOS MODULOS
from .models import Book, Copy, Publication

# Permisos
class ViewPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class CreatePermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == "create" or request.method == 'POST': 
            return request.user.rol == 4
        return True

# Create your views here.
class BookViewSet(ModelViewSet):            # VISTA DE LOS LIBROS
    serializer_class = BookSerializer
    queryset = Book.objects.all()           # con esto se muestran todos los atributos
    permission_classes = [CreatePermission, ViewPermission]  # Asignamos Permisos 

class CopyViewSet(ModelViewSet):            # VISTA DE LAS COPIAS
    serializer_class = CopySerializer
    queryset = Copy.objects.all()
    permission_classes = [CreatePermission, IsAuthenticated]

class PublicationViewSet(ModelViewSet):     # VISTA DE LAS PUBLICACIONES
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()