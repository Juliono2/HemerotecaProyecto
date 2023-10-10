from rest_framework import serializers
from .models import Book
from .models import Copy
from .models import Publication

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = "__all__"

from rest_framework import serializers
from .models import Publication

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"