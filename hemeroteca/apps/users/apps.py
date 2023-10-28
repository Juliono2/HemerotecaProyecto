from django.apps import AppConfig

# Configuraciones para la aplicacion
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'     # apps es la capeta donde esta contenido, users es la app
