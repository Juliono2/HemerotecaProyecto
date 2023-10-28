from django.db import models
from django.core.exceptions import ValidationError

#IMPORTACIONES DE MODELOS EN OTRAS APPS
from apps.books.models import Copy

# Create your models here.
class Shelf(models.Model):                  # Modelo de estante con sus atributos
    number = models.CharField(max_length=3, null=False, blank=False)
    #capacity

    def save(self, *args, **kwargs):        # Validamos que el número tenga exactamente tres dígitos
        if not self.number.isdigit() or len(self.number) != 3:
            raise ValidationError("El número del estante debe tener exactamente tres dígitos.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.number

class Section(models.Model):                # Modelo de seccion con sus atributos
    name = models.CharField(max_length=50, null=False, blank=False)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)      # Llave foranea desde Estante
    #description

    def __str__(self):
        return self.name

class BookLocation(models.Model):            # Modelo de localizacion del libro con sus atributos
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)            # Llave foranea desde Copia
    section = models.ForeignKey(Section, on_delete=models.CASCADE)      # Llave foranea desde Seccion

    def __str__(self):
        return f"Shelf: {self.section.shelf}, Section: {self.section}, Copy: {self.copy}"
