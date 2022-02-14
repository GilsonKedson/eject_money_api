from django.urls import path, include
from rest_framework import routers
from transacoes.viewsets import TransactionViewSet
'''
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="EJECT MONEY API",
      default_version='v1',
      description="API PARA TRILHA REACT JS",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
'''

router = routers.DefaultRouter()
router.register('transacoes', TransactionViewSet, basename='transacao')

urlpatterns = [
    path('', include(router.urls)),
    #path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
