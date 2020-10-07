from .models import Sabor, Sorvete
from django.test import TestCase
from decimal import Decimal

class TestModelSabot(TestCase):
    def setUp(self):
        self.sabor = Sabor(nome_do_sabor='abacate')

    def test_str_de_sabor_retorna_seu_nome(self):
        esperado = 'abacate'
        resultado = str(self.sabor)
        self.assertEqual(esperado, resultado)

class TestModelSorvete(TestCase):
    def setUp(self):
        self.sorvete = Sorvete.objects.create(
            unidades=10,
            preco_de_custo=0.5
        )

        self.sabor = Sabor.objects.create(nome_do_sabor='abacate')

        self.sorvete.sabores.set((self.sabor, ))

    def test_str_retorna_o_nome_do_sabor_e_o_preco_de_venda(self):
        esperado = 'abacate 0'
        resultado = str(self.sorvete)
        self.assertEqual(esperado, resultado)

    def test_calcula_preco_de_venda_deve_retornar_10_porcento_a_mais(self):
        sorvete = Sorvete.objects.create(
            unidades=10,
            preco_de_custo=0.5
        )
        
        esperado = Decimal('0.55')
        resultado = self.sorvete.calcula_preco_de_venda()
        self.assertEqual(esperado, resultado)

    def test_calcula_preco_de_venda_deve_retornar_20_porcento_a_mais(self):
        sorvete = Sorvete.objects.create(
            unidades=10,
            preco_de_custo=4.99
        )

        esperado = Decimal('5.98')
        resultado = sorvete.calcula_preco_de_venda()
        self.assertEqual(esperado, resultado)

    def test_calcula_preco_de_venda_deve_retornar_35_porcento_a_mais(self):
        sorvete = Sorvete.objects.create(
            unidades=10,
            preco_de_custo=6
        )

        esperado = Decimal('8.1')
        resultado = sorvete.calcula_preco_de_venda()
        self.assertEqual(esperado, resultado)