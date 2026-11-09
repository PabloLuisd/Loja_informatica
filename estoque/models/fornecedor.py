from django.db import models


class Fornecedor(models.Model):

    nome = models.CharField(max_length=150)

    cnpj = models.CharField(
        max_length=18,
        unique=True
    )

    telefone = models.CharField(max_length=20)

    email = models.EmailField()

    class Meta:
        ordering = ['nome']
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome