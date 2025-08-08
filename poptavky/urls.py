from django.urls import path, include
from rest_framework import routers
from .views import PoptavkaViewSet
from .views import odeslat_poptavku

router = routers.DefaultRouter()
router.register(r'poptavky', PoptavkaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', odeslat_poptavku, name='odeslat_poptavku'),
]
