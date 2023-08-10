from typing import Iterable, Optional
from django.db import models
from django.utils import timezone
from pessoas.models import Pessoa


class MetaConsumo (models.Model):
    meta_consumo = models.IntegerField(blank=True)
    data = models.DateField(auto_now_add=True)

    pessoa = models.ForeignKey(
        "pessoas.Pessoa",
        on_delete=models.CASCADE,
        related_name="metas_consumo"
    )

    def __str__(self) -> str:
        return f"({self.id} Consumos do dia {self.data})"



class Consumo(models.Model):
    quantidade = models.PositiveIntegerField (help_text = "Por favor, inserir valor inteiro em ml")
    criado_em = models.DateField(auto_now_add = True)

    pessoa = models.ForeignKey(
        "pessoas.Pessoa",
        on_delete=models.CASCADE,
        related_name="consumos"
    )

    meta_diaria = models.ForeignKey(
        "consumos.MetaConsumo",
        on_delete=models.CASCADE,
        related_name="consumos"
    )

    def __str__(self):
        return f"({self.id}) {self.quantidade}ml"
    
