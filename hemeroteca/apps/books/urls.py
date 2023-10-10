from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CopyViewSet, PublicationViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename="book")
router.register(r'copy', CopyViewSet, basename="copy")
router.register(r'publication', PublicationViewSet, basename="publication")

urlpatterns = []
urlpatterns += router.urls