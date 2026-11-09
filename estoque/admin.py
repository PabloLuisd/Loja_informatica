from django.contrib import admin
from .models import Categoria, Fornecedor, Produto, MovimentacaoEstoque
admin.site.register(Categoria)
admin.site.register(Fornecedor)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','categoria','fornecedor','preco','quantidade_estoque')
    list_filter = ('categoria','fornecedor')
    search_fields = ('nome',)
@admin.register(MovimentacaoEstoque)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto','tipo','quantidade','data_movimentacao')
    list_filter = ('tipo','data_movimentacao')
