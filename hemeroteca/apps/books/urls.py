# IMPORTACIONES DE REST
from rest_framework.routers import DefaultRouter

# IMPORTACIONES DE LAS VISTAS
from .views import BookViewSet, CopyViewSet, PublicationViewSet

# Crear un enrutador para las vistas
router = DefaultRouter()
router.register(r'books', BookViewSet, basename="book")
router.register(r'copy', CopyViewSet, basename="copy")
router.register(r'publication', PublicationViewSet, basename="publication")

urlpatterns = []
urlpatterns += router.urls  # Agregado de las Urls generadas