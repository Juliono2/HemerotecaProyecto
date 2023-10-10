from django.shortcuts import render

from .serializers import AuthorSerializer, UserSerializer, SuscriptionSerializer
from .models import Author, User, Suscription
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class SuscriptionViewSet(ModelViewSet):
    serializer_class = SuscriptionSerializer
    queryset = Suscription.objects.all()

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data
        
        _Suscription = Suscription.objects.filter(
            user_id=data.get("user"),
            start_date__lt=data.get('end_date'),
            end_date__gt=data.get('end_date')
        )
        if len(_Suscription)>0:
            return Response({"error": "Ya tienes una suscripción activa."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)
