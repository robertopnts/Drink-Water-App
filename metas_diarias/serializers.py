from rest_framework import serializers
from .models import MetaConsumo


class MetaConsumoSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    meta_consumo = serializers.IntegerField(required=False)
    data = serializers.DateField(read_only=True)

    pessoa = serializers.CharField(read_only=True, source="pessoa.nome")
    consumos = serializers.ListField(read_only=True, source="consumo")

    def create(self, validated_data: dict) -> MetaConsumo:
        return MetaConsumo.objects.create(**validated_data)