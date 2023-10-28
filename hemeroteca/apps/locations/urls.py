# IMPORTACIONES DE REST
from rest_framework.routers import DefaultRouter

# IMPORTACIONES DE LAS VISTAS
from .views import BookLocationViewSet, ShelfViewSet, SectionViewSet

# Crear un enrutador para las vistas
router = DefaultRouter()
router.register(r'book-location', BookLocationViewSet, basename="book-location")
router.register(r'shelf', ShelfViewSet, basename="shelf")
router.register(r'section', SectionViewSet, basename="section")

urlpatterns = []
urlpatterns += router.urls    # Agregado de las Urls generadas