from rest_framework import serializers
from .models import Consumo
from pessoas.models import Pessoa
from metas_diarias.models import MetaConsumo

class ConsumoSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    quantidade = serializers.IntegerField()
    criado_em = serializers.DateField(read_only=True)

    pessoa = serializers.PrimaryKeyRelatedField(queryset=Pessoa.objects.all())
    meta_diaria = serializers.PrimaryKeyRelatedField(queryset=MetaConsumo.objects.all())

    def create(self, validated_data: dict) -> Consumo:
        return Consumo.objects.create(**validated_data)