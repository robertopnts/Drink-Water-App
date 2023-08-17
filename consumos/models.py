from django.db import models
from pessoas.models import Pessoa


class Consumo(models.Model):
    quantidade = models.IntegerField (help_text = "Por favor, inserir valor inteiro em ml")
    criado_em = models.DateField(auto_now_add = True)

    pessoa = models.ForeignKey(
        "pessoas.Pessoa",
        on_delete=models.CASCADE,
        related_name="consumos"
    )

    meta_diaria = models.ForeignKey(
        "metas_diarias.MetaConsumo",
        on_delete=models.CASCADE,
        related_name="consumos"
    )

    def __str__(self):
        return f"({self.id}) {self.quantidade}ml"
    
