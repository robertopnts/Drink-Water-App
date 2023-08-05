from django.db import models


class Pessoa (models.Model):
    nome = models.CharField(max_length=127)
    peso = models.DecimalField(max_digits=5,decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.peso}kgs"
    
