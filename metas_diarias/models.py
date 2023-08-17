from django.db import models

# Create your models here.
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