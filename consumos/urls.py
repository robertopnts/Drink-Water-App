from django.urls import path
from .views import ConsumoView


urlpatterns = [
    path("pessoa/<int:pessoa_id>/consumo/", ConsumoView.as_view())
]