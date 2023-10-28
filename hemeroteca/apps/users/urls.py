# IMPORTACIONES DE REST
from rest_framework.routers import DefaultRouter

# IMPORTACIONES DE LAS VISTAS
from .views import AuthorViewSet, UserViewSet, SuscriptionViewSet

# Crear un enrutador para las vistas
router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename="author")
router.register(r'users', UserViewSet, basename="user")
router.register(r'suscriptions', SuscriptionViewSet, basename="suscription")

urlpatterns = []
urlpatterns += router.urls  # Agregado de las Urls generadas