from django.test import TestCase
from consumos.models import Consumo


class ConsumoTestCase (TestCase):
    @classmethod
    def setUpTestData(self):
        Consumo.objects.create(quantidade=200)

    def test_consumo_was_created(self):
        consumo1 = Consumo.objects.get(id=1)
        self.assertEqual(consumo1.quantidade, 200)
        