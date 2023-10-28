from django.shortcuts import render
# IMPORTACIONES DE REST
from rest_framework.viewsets import ModelViewSet

# IMPORTACIONES DE SERIALIZERS
from .serializers import BookLocationSerializer, SectionSerializer, ShelfSerializer

# IMPORTACIONES DE LOS MODULOS
from .models import BookLocation, Shelf, Section

# Create your views here.
class BookLocationViewSet(ModelViewSet):            # VISTA DE LAS UBICACIONES
    serializer_class = BookLocationSerializer
    queryset = BookLocation.objects.all()

class SectionViewSet(ModelViewSet):            # VISTA DE LAS SECCIONES
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

class ShelfViewSet(ModelViewSet):            # VISTA DE LOS ESTANTES
    serializer_class = ShelfSerializer
    queryset = Shelf.objects.all()
