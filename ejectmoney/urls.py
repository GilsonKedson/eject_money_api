from django.urls import path, include
from rest_framework import routers
from transacoes.viewsets import TransactionViewSet

router = routers.DefaultRouter()
router.register('transacoes', TransactionViewSet, basename='transacao')

urlpatterns = [
    path('', include(router.urls)),
]
