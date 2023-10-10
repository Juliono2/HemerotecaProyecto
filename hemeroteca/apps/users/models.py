from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Suscription(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField() 
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Author(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.name}"