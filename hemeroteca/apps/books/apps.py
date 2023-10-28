from django.apps import AppConfig

# Configuraciones para la aplicacion
class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.books'     # apps es la capeta donde esta contenido, book es la app
