from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Loan
from .serializers import LoanSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class LoanViewSet(ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        _Loan = Loan.objects.filter(
            date_loan__lt=data.get("date_loan"),
            date_end__gt=data.get("date_loan"),
            copy_id=data.get("copy")
        )
        if len(_Loan)>0:
            return Response({"error": "Ya existe un préstamo activo para esta copia."}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

       