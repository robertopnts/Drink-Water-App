from rest_framework import serializers
from .models import Pessoa


class PessoaSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=127)
    peso = serializers.DecimalField(max_digits=5,decimal_places=2)
    criado_em = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict) -> Pessoa:
        return Pessoa.objects.create(**validated_data)