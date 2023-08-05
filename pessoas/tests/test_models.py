from django.test import TestCase
from pessoas.models import Pessoa


class PessoaTestCase (TestCase):
    @classmethod
    def setUpTestData(self):
         Pessoa.objects.create(
              nome="Pessoa Teste 1",
              peso=70.5
         )

    def test_pessoa_was_created(self):
         pessoa1 = Pessoa.objects.get(id=1)
         self.assertEqual(pessoa1.nome, "Pessoa Teste 1")