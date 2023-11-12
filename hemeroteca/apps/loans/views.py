from django.shortcuts import render
from django.db import models
from django.utils import timezone

# IMPORTACIONES DE REST
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
# Rest para permisos
from rest_framework.permissions import IsAuthenticated, BasePermission

# IMPORTACIONES DE SERIALIZERS
from .serializers import LoanSerializer, LateLoanSerializer, DebtSerializer

# IMPORTACIONES DE LOS MODULOS
from .models import Loan, LateLoan, Debt

# Permisos
class ViewPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class BibliotecarioOrAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.rol in [1, 4]   # Verifica si el usuario tiene el rol de Bibliotecario o Administrador

# Create your views here.
class LoanViewSet(ModelViewSet):                # VISTA DE LOS PRESTAMOS
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    permission_classes = [ViewPermission | BibliotecarioOrAdminPermission]  # Asignamos Permisos

    def create(self, request, *args, **kwargs):         # Modificamos el Query de Creacion
        # Obtener el serializador y validar los datos de la solicitud.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        #Verificamos si ya existe un préstamo activo para la misma copia.
        _Loan = Loan.objects.filter(
            #date_loan__lt=data.get("date_loan"),
            #date_end__gt=data.get("date_loan"),
            active= True,                   # Filtramos por prestamos activos.
            copy_id=data.get("copy")        # Tambien por la copia que presenta interes
        ).filter(
            # Comprobar si existe algún solapamiento de fechas entre préstamos.
            (models.Q(date_loan__lt=data.get("date_loan"), date_end__gt=data.get("date_loan")) |
            models.Q(date_loan__lt=data.get("date_end"), date_end__gt=data.get("date_end")) |
            models.Q(date_loan__gte=data.get("date_loan"), date_end__lte=data.get("date_end")))
        )
        if len(_Loan)>0:
            # Si se encuentra un préstamo activo para la misma copia, devolver un error.
            return Response({"error": "Ya existe un préstamo activo para esta copia."}, status=status.HTTP_400_BAD_REQUEST)
        # Si no existe un préstamo activo para la copia, continuar con la creación.
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):         # Modificamos el query de Actualizacion
        # Apartamos el objeto a actualizar
        instance = self.get_object()        
        # Obtenemos serializador y validamos
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)     # Indicamos el update

        current_date = timezone.now()   # Fecha actual
        
        # Verificar si el préstamo está en retardo y no está marcado como activo.
        if current_date > instance.date_end and not instance.active:
            late_days = (current_date - instance.date_end).days     # Diferencia entre prestamo y fecha actual
            price_per_day = 600                     # Tarifa por dia
            late_fee = price_per_day * late_days    # Valor por mora

            # Se genera el retardo y se guarda
            late_loan = LateLoan(days_late=late_days, late_fee=late_fee, loan=instance)
            late_loan.save()

            # Se genera la deuda y se guarda
            debt = Debt(amount=late_fee, user=instance.user)
            debt.save()

            # Se indica que se ha generado una deuda
            return Response({"error": "Préstamo en retardo. Se ha generado una deuda de ${:.2f}".format(late_fee)}, status=status.HTTP_200_OK)
        # Si no hay retardo o el préstamo sigue activo, continuar con la actualización.
        return Response(serializer.data)
    
class LateLoanViewSet(ModelViewSet):            # VISTA DE LOS RETARDOS
    serializer_class = LateLoanSerializer
    queryset = LateLoan.objects.all()
    permission_classes = [ViewPermission | BibliotecarioOrAdminPermission]  # Asignamos Permisos


class DebtViewSet(ModelViewSet):            # VISTA DE LOS DEUDAS
    serializer_class = DebtSerializer
    queryset = Debt.objects.all()
    permission_classes = [ViewPermission | BibliotecarioOrAdminPermission]  # Asignamos Permisos

       