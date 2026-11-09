from django.db import models
from .produto import Produto


class MovimentacaoEstoque(models.Model):

    ENTRADA = 'Entrada'
    SAIDA = 'Saída'

    TIPOS = [
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída'),
    ]

    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT,
        related_name='movimentacoes'
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPOS
    )

    quantidade = models.PositiveIntegerField()

    data_movimentacao = models.DateTimeField(
        auto_now_add=True
    )

    observacao = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ['-data_movimentacao']
        verbose_name = 'Movimentação de Estoque'
        verbose_name_plural = 'Movimentações de Estoque'

    def __str__(self):
        return f'{self.tipo} - {self.produto} ({self.quantidade})'