from django.db import models


class Consumo(models.Model):
    quantidade = models.IntegerField(help_text = "Por favor, inserir valor inteiro em ml")
    criado_em = models.TimeField(auto_now_add = True)

    def recipiente(self):
        return f"{self.quantidade}ml de água"