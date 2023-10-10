from rest_framework import serializers
from .models import Author, Suscription
from django.contrib.auth import get_user_model

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class SuscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscription
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'first_name', 'last_name')