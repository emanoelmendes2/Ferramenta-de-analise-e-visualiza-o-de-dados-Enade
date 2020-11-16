from ..models import *
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Permission

class DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = '__all__'

class EnadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enade
        fields = '__all__'