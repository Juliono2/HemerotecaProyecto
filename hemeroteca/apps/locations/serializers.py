# IMPORTACIONES DE REST
from rest_framework import serializers

# IMPORTACIONES DE LOS MODELOS
from .models import Section, Shelf, BookLocation

class BookLocationSerializer(serializers.ModelSerializer):  # Serializador del modelo UbicacionLibro
    """
    Serializador para el modelo BookLocation.

    Este serializador se utiliza para convertir instancias del modelo BookLocation
    en datos JSON y viceversa.

    Atributos:
    model (BookLocation): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = BookLocation
        fields = "__all__"

class SectionSerializer(serializers.ModelSerializer):   # Serializador del modelo Seccion
    """
    Serializador para el modelo Section.

    Este serializador se utiliza para convertir instancias del modelo Section
    en datos JSON y viceversa.

    Atributos:
    model (Section): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = Section
        fields = "__all__"

class ShelfSerializer(serializers.ModelSerializer):     # Serializador del modelo Estante
    """
    Serializador para el modelo Shelf.

    Este serializador se utiliza para convertir instancias del modelo Shelf
    en datos JSON y viceversa.

    Atributos:
    model (Shelf): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = Shelf
        fields = "__all__"