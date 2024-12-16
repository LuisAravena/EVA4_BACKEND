from rest_framework import serializers
from .models import Numero, Reporte, Usuario

class NumeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numero
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
