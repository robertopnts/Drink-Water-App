from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from .serializers import PessoaSerializer
from .models import Pessoa

# Create your views here.
class PessoaView(APIView):
    def post(self, request: Request) -> Response:
        serializer = PessoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def get(self, request: Request) -> Response:
        pessoas = Pessoa.objects.all().order_by("id")

        serializer = PessoaSerializer(pessoas, many=True)

        return Response(serializer.data)
    
  
class PessoaDetailedView(APIView):
    def get(self, request: Request, pessoa_id: int) -> Response:
        pessoa = get_object_or_404(Pessoa, id=pessoa_id)

        serializer = PessoaSerializer(pessoa)

        return Response(serializer.data)