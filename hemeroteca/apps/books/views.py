from django.shortcuts import render
# IMPORTACIONES DE REST
from rest_framework.viewsets import ModelViewSet

# IMPORTACIONES DE SERIALIZERS
from .serializers import BookSerializer, CopySerializer, PublicationSerializer

# IMPORTACIONES DE LOS MODULOS
from .models import Book, Copy, Publication


# Create your views here.
class BookViewSet(ModelViewSet):            # VISTA DE LOS LIBROS
    serializer_class = BookSerializer
    queryset = Book.objects.all()           # con esto se muestran todos los atributos

class CopyViewSet(ModelViewSet):            # VISTA DE LAS COPIAS
    serializer_class = CopySerializer
    queryset = Copy.objects.all()

class PublicationViewSet(ModelViewSet):     # VISTA DE LAS PUBLICACIONES
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()