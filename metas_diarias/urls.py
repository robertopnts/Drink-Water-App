
from django.urls import path
from .views import MetasConsumoView, MetaConsumoDetalhadaView


urlpatterns = [
    path("pessoa/<int:pessoa_id>/diario/", MetasConsumoView.as_view()),
    path("diario/<int:diario_id>/", MetaConsumoDetalhadaView.as_view())
]