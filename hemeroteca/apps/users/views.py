from django.shortcuts import render

# IMPORTACIONES DE REST
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

# IMPORTACIONES DE SERIALIZERS
from .serializers import AuthorSerializer, UserSerializer, SuscriptionSerializer

# IMPORTACIONES DE LOS MODULOS
from .models import Author, User, Suscription

# Create your views here.
class AuthorViewSet(ModelViewSet):          # VISTA DE LOS AUTORES
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()         # con esto se muestran todos los atributos

class UserViewSet(ModelViewSet):            # VISTA DE LOS USUARIOS
    serializer_class = UserSerializer
    queryset = User.objects.all()

class SuscriptionViewSet(ModelViewSet):     # VISTA DE LAS SUSCRIPCIONES
    serializer_class = SuscriptionSerializer
    queryset = Suscription.objects.all()

    def create(self, request, *args, **kwargs):     # Modificamos el Query de Creacion
        
        # Obtener el serializador y validar los datos de la solicitud.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data
        
        # Verificar si ya existe una suscripción activa para el usuario.
        _Suscription = Suscription.objects.filter(
            user_id=data.get("user"),                   # Filtrar por el ID de usuario.
            start_date__lt=data.get('end_date'),        # La fecha de inicio debe ser anterior a la fecha de finalización.
            end_date__gt=data.get('end_date')           # La fecha de finalización debe ser posterior a la fecha de finalización.
        )
        if len(_Suscription)>0: # Si se encuentra una suscripción activa, devolver un error.
            return Response({"error": "Ya tienes una suscripción activa."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Si no hay una suscripción activa, continuar con la creación.
        return super().create(request, *args, **kwargs)
