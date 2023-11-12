from django.urls import path, include

# IMPORTACIONES DE REST
from rest_framework.routers import DefaultRouter

# IMPORTACIONES DE LAS VISTAS
from .views import AuthorViewSet, SuscriptionViewSet, CreateUserView

# Crear un enrutador para las vistas
router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename="author")
#router.register(r'users', UserViewSet, basename="user")
router.register(r'suscriptions', SuscriptionViewSet, basename="suscription")

urlpatterns = [
    path('sign-up/',CreateUserView.as_view(),name='create_user')
]
urlpatterns += router.urls  # Agregado de las Urls generadas