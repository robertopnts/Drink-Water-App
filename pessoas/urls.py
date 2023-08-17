from django.urls import path
from .views import PessoaView, PessoaDetailedView


urlpatterns = [
    path("pessoa/", PessoaView.as_view()),
    path("pessoa/<int:pessoa_id>/", PessoaDetailedView.as_view())
]