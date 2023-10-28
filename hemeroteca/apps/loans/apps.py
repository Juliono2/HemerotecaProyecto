from django.apps import AppConfig

# Configuraciones para la aplicacion
class LoansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.loans'     # apps es la capeta donde esta contenido, loans es la app
