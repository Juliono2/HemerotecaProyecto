# IMPORTACIONES DE REST
from rest_framework import serializers

# IMPORTACIONES DE LOS MODELOS
from .models import Book
from .models import Copy
from .models import Publication

class BookSerializer(serializers.ModelSerializer):  # Serializador del modelo Libro
    """
    Serializador para el modelo Book.

    Este serializador se utiliza para convertir instancias del modelo Book
    en datos JSON y viceversa.

    Atributos:
    model (Book): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = Book
        fields = "__all__"

class CopySerializer(serializers.ModelSerializer):  # Serializador del modelo Copia
    """
    Serializador para el modelo Copy.

    Este serializador se utiliza para convertir instancias del modelo Copy
    en datos JSON y viceversa.

    Atributos:
    model (Copy): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = Copy
        fields = "__all__"

class PublicationSerializer(serializers.ModelSerializer):   # Serializador del modelo Publicacion
    """
    Serializador para el modelo Publication.

    Este serializador se utiliza para convertir instancias del modelo Publication
    en datos JSON y viceversa.

    Atributos:
    model (Publication): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = Publication
        fields = "__all__"