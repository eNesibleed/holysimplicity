from django.urls import path, include
from rest_framework import routers
from .views import PoptavkaViewSet

router = routers.DefaultRouter()
router.register(r'poptavky', PoptavkaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
