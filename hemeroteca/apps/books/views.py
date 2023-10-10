from django.shortcuts import render

from .serializers import BookSerializer, CopySerializer, PublicationSerializer
from .models import Book, Copy, Publication
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CopyViewSet(ModelViewSet):
    serializer_class = CopySerializer
    queryset = Copy.objects.all()

class PublicationViewSet(ModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()