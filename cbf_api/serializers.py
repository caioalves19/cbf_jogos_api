from dataclasses import field
from rest_framework import serializers
from cbf_api.models import Jogo

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'