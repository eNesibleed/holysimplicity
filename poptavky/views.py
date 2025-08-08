from django.shortcuts import render

from rest_framework import viewsets
from .models import Poptavka
from .serializers import PoptavkaSerializer

class PoptavkaViewSet(viewsets.ModelViewSet):
    queryset = Poptavka.objects.all().order_by('-datum')
    serializer_class = PoptavkaSerializer

