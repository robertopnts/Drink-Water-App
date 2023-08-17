from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404, get_list_or_404
from pessoas.models import Pessoa
from .models import Consumo
from metas_diarias.models import MetaConsumo
from consumos.serializers import ConsumoSerializer
from django.utils import timezone
import math


# Create your views here.
class ConsumoView(APIView):
    def post(self, request: Request, pessoa_id: int) -> Response:
        pessoa = get_object_or_404(Pessoa, id=pessoa_id)
        hoje = timezone.datetime.now().date()

        diario = MetaConsumo.objects.filter(
            data__iexact=hoje,
            pessoa=pessoa
        ).first()

        if not diario: 
            agua_diaria = math.ceil(float(pessoa.peso) * 35)
            diario = MetaConsumo.objects.create(meta_consumo=agua_diaria, pessoa=pessoa)

        consumo_obj = request.data
        consumo_obj["pessoa"] = pessoa.id
        consumo_obj["meta_diaria"] = diario.id

        serializer = ConsumoSerializer(data=consumo_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save(pessoa=pessoa, meta_diaria=diario)
        
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def get(self, request: Request, pessoa_id: int) -> Response:
        consumos = Consumo.objects.filter(
            pessoa__exact=pessoa_id
        )

        serializer = ConsumoSerializer(consumos, many=True)

        return Response(serializer.data)