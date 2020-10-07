from django.db import models
from decimal import Decimal, ROUND_DOWN

class Sabor(models.Model):
    nome_do_sabor = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_do_sabor

class Sorvete(models.Model):
    unidades = models.PositiveIntegerField('Unidades')
    sabores = models.ManyToManyField('Sabor')
    
    preco_de_venda = models.DecimalField(
        'Preço de Venda',
        max_digits=6,
        decimal_places=2,
        default=Decimal('0')
    )
    
    preco_de_custo = models.DecimalField(
        'Preço de Custo',
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        sabores = ''.join(str(sabor) for sabor in self.sabores.all())
        exibicao = f'{sabores} {str(self.preco_de_venda).replace(".", ",")}'

        return exibicao
    
    def calcula_preco_de_venda(self):
        """
            Calcula preço de venda de uma unidade do sorvete.
        """
        preco_de_custo = self.preco_de_custo * 10
        if preco_de_custo <= Decimal('24.99'):
            self.preco_de_venda = (
                self.preco_de_custo + (self.preco_de_custo * 0.1)
            )
        elif preco_de_custo <= Decimal('49.99'):
            self.preco_de_venda = (
                self.preco_de_custo + (self.preco_de_custo * 0.2)
            )
        else:
            self.preco_de_venda = (
                self.preco_de_custo + (self.preco_de_custo * 0.35)
            )
            
        self.save()

        return Decimal(str(self.preco_de_venda)).quantize(
                Decimal('0.01'),
                rounding=ROUND_DOWN
            )