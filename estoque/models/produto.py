from django.db import models
from .categoria import Categoria
from .fornecedor import Fornecedor


class Produto(models.Model):

    nome = models.CharField(max_length=150)

    descricao = models.TextField(
        blank=True
    )

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantidade_estoque = models.PositiveIntegerField(
        default=0
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='produtos'
    )

    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.PROTECT,
        related_name='produtos'
    )

    class Meta:
        ordering = ['nome']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome

    @property
    def estoque_baixo(self):
        return self.quantidade_estoque <= 5