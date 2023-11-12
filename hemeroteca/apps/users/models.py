from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):                   # Se hace uso del modelo de AbstractUser
    ROLES_HEMEROTECA = (
        (1,'Bibliotecario'),
        (2,'Catalogador'),
        (3,'Lector'),
        (4,'Administrador')
    )

    REQUIRED_FIELDS = ["email"]             # Con esto hacemos que los atributos contenidos sean obligatorios
    rol = models.IntegerField(choices=ROLES_HEMEROTECA, default=3)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Suscription(models.Model):            # Modelo de Suscripcion con sus atributos
    start_date = models.DateTimeField()
    end_date = models.DateTimeField() 
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) # Llave foranea desde Usuario

class Author(models.Model):                 # Modelo de Autor con sus atributos
    name = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.name}"