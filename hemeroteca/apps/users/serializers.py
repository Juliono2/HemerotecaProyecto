from django.contrib.auth import get_user_model

# IMPORTACIONES DE REST
from rest_framework import serializers

# IMPORTACIONES DE LOS MODELOS
from .models import Author, Suscription, User

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Author.

    Este serializador se utiliza para convertir instancias del modelo Author
    en datos JSON y viceversa.

    Atributos:
    model (Author): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = Author
        fields = "__all__"

class SuscriptionSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Suscription.

    Este serializador se utiliza para convertir instancias del modelo Suscription
    en datos JSON y viceversa.

    Atributos:
    model (Suscription): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = Suscription
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo de Usuario.

    Este serializador se utiliza para convertir instancias del modelo de Usuario
    en datos JSON y viceversa.

    Atributos:
    model (User): El modelo que se serializa.
    fields (tuple): Una tupla de campos que se incluirán en la serialización,
    que incluye 'id', 'username', 'email', 'first_name' y 'last_name'.
    """
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        _user = User.objects.create_user(
            username=validated_data['email'],
            password=validated_data['password'],
            email = validated_data['email'],
            rol=validated_data.get('rol', 3)
        )

        return _user
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'rol')