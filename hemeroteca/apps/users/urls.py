from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, UserViewSet, SuscriptionViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename="author")
router.register(r'users', UserViewSet, basename="user")
router.register(r'suscriptions', SuscriptionViewSet, basename="suscription")

urlpatterns = []
urlpatterns += router.urls