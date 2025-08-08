from rest_framework import serializers
from .models import Poptavka

class PoptavkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poptavka
        fields = '__all__'
