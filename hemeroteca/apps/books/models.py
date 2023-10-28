from django.db import models

#IMPORTACIONES DE MODELOS EN OTRAS APPS
from apps.users.models import Author

# Create your models here.
class Book(models.Model):               # Modelo de libro con sus atributos
    name = models.CharField(max_length=250, null=False, blank=False)
    edition = models.IntegerField()
    date_publication = models.DateField(null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)     # Llave foranea desde Autor

    def __str__(self):
        return f"{self.id} - {self.name}"
    
class Copy(models.Model):               # Modelo de copia con sus atributos
    state = models.CharField(max_length=50, null=False, blank=False)
    ubication  = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null=False, blank=False) # Llave foranea desde Libro

    def __str__(self):
        return f"{self.id} - {self.book.name}"

class Publication(models.Model):        # Modelo de publicaciones con sus atributos
    date = models.DateField()
    frecuency = models.IntegerField()