# IMPORTACIONES DE REST
from rest_framework import serializers

# IMPORTACIONES DE LOS MODELOS
from .models import Loan, LateLoan, Debt

class LoanSerializer(serializers.ModelSerializer):  # Serializador del modelo Prestamo
    """
    Serializador para el modelo Loan.

    Este serializador se utiliza para convertir instancias del modelo Loan
    en datos JSON y viceversa.

    Atributos:
    model (Loan): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = Loan
        fields = "__all__"

class LateLoanSerializer(serializers.ModelSerializer): # Serializador del modelo Retardos
    """
    Serializador para el modelo LateLoan.

    Este serializador se utiliza para convertir instancias del modelo LateLoan
    en datos JSON y viceversa.

    Atributos:
    model (LateLoan): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = LateLoan
        fields = "__all__"

class DebtSerializer(serializers.ModelSerializer):  # Serializador del modelo Deudas
    """
    Serializador para el modelo Debt.

    Este serializador se utiliza para convertir instancias del modelo Debt
    en datos JSON y viceversa.

    Atributos:
    model (Debt): El modelo que se serializa.
    fields (str): Una lista de campos que se incluirán en la serialización.
    """
    class Meta:
        model = Debt
        fields = "__all__"