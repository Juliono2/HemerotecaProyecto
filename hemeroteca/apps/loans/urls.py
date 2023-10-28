# IMPORTACIONES DE REST
from rest_framework.routers import DefaultRouter

# IMPORTACIONES DE LAS VISTAS
from .views import LoanViewSet, LateLoanViewSet, DebtViewSet

# Crear un enrutador para las vistas
router = DefaultRouter()
router.register(r'loans', LoanViewSet, basename="loan")
router.register(r'lateloans', LateLoanViewSet, basename="lateloan")
router.register(r'debts', DebtViewSet, basename="debt")

urlpatterns = []
urlpatterns += router.urls  # Agregado de las Urls generadas
