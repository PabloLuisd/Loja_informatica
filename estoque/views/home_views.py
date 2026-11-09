from django.shortcuts import render
from ..models import (
    Produto,
    Categoria,
    Fornecedor,
    MovimentacaoEstoque
)


def dashboard(request):
    context = {
        'total_produtos': Produto.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'total_fornecedores': Fornecedor.objects.count(),
        'total_movimentacoes': MovimentacaoEstoque.objects.count(),
        'produtos_baixo': Produto.objects.filter(
            quantidade_estoque__lte=5
        ),
    }

    return render(request, 'estoque/dashboard.html', context)