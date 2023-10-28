from django.db import models

#IMPORTACIONES DE MODELOS EN OTRAS APPS
from apps.users.models import User
from apps.books.models import Copy

# Create your models here.
class Loan(models.Model):                       # Modelo de prestamo con sus atributos
    date_loan = models.DateTimeField()
    date_end = models.DateTimeField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)     # Llave foranea desde Usuario
    copy = models.ForeignKey(Copy, on_delete=models.DO_NOTHING)     # Llave foranea desde Copia
    
    def __str__(self):
        return f"{self.user}"
    
    def __str__(self):
        return f"{self.copy}"
    
class LateLoan(models.Model):                   # Modelo de retardos con sus atributos
    days_late = models.PositiveIntegerField()
    late_fee = models.DecimalField(max_digits=10, decimal_places=2)
    loan = models.OneToOneField(Loan, on_delete=models.CASCADE)     #Llave foranea desde Prestamo

class Debt(models.Model):                       # Modelo de deudas con sus atributos
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_generated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)        # Llave foranea desde Usuario
