from rest_framework.views import APIView, Request, Response, status
from .models import MetaConsumo
from consumos.models import Consumo
from consumos.serializers import ConsumoSerializer
from .serializers import MetaConsumoSerializer

# Create your views here.
class MetasConsumoView(APIView):
    def get(self, request: Request, pessoa_id: int) -> Response:
        metas = MetaConsumo.objects.filter(
            pessoa__exact=pessoa_id
        ).order_by("-id")

        diarios_serializer = MetaConsumoSerializer(metas, many=True)

        diarios = diarios_serializer.data
        for diario in diarios:
            consumos_dia = Consumo.objects.filter(
                meta_diaria__exact=diario["id"]
            )
            consumo_serializer = ConsumoSerializer(consumos_dia, many=True)
            consumos_dia = consumo_serializer.data
            
            consumido = 0
            for consumo in consumos_dia:
                consumido += consumo["quantidade"]

            diario["consumiu"] = consumido

        
        return Response(diarios)
    
class MetaConsumoDetalhadaView(APIView):
    def get(self,request: Request, diario_id: int) -> Response:
        print(diario_id)
        meta = MetaConsumo.objects.filter(
            id=diario_id
        ).first()
        
        consumos = Consumo.objects.filter(
            meta_diaria__exact=diario_id
        )

        consumo_serializer = ConsumoSerializer(consumos, many=True)

        diario_serializer = MetaConsumoSerializer(meta)

        diario_obj = diario_serializer.data
        diario_obj["consumos"] = consumo_serializer.data

        return Response(diario_obj)