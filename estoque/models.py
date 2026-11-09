from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Categorias'
    def __str__(self): return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    class Meta: ordering = ['nome']
    def __str__(self): return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name='produtos')
    class Meta: ordering = ['nome']
    def __str__(self): return self.nome
    @property
    def estoque_baixo(self): return self.quantidade_estoque <= 5

class MovimentacaoEstoque(models.Model):
    ENTRADA = 'Entrada'
    SAIDA = 'Saída'
    TIPOS = [(ENTRADA, 'Entrada'), (SAIDA, 'Saída')]
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='movimentacoes')
    tipo = models.CharField(max_length=10, choices=TIPOS)
    quantidade = models.PositiveIntegerField()
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True)
    class Meta: ordering = ['-data_movimentacao']
    def __str__(self): return f'{self.tipo} - {self.produto} ({self.quantidade})'
