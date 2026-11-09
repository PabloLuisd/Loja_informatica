from django.shortcuts import render, redirect, get_object_or_404
from ..models import Produto
from ..forms import ProdutoForm


def produto_lista(request):
    produtos = Produto.objects.select_related(
        'categoria', 'fornecedor'
    ).all()

    busca = request.GET.get('busca')

    if busca:
        produtos = produtos.filter(nome__icontains=busca)

    return render(request, 'estoque/produto_lista.html', {
        'produtos': produtos,
        'busca': busca
    })


def produto_criar(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('estoque:produto_lista')

    return render(request, 'estoque/formulario.html', {
        'form': form,
        'titulo': 'Novo Produto'
    })


def produto_editar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('estoque:produto_lista')

    return render(request, 'estoque/formulario.html', {
        'form': form,
        'titulo': 'Editar Produto'
    })


def produto_excluir(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        produto.delete()
        return redirect('estoque:produto_lista')

    return render(request, 'estoque/confirmar_exclusao.html', {
        'objeto': produto,
        'titulo': 'Excluir Produto'
    })


def estoque_baixo(request):
    produtos = Produto.objects.filter(
        quantidade_estoque__lte=5
    )

    return render(request, 'estoque/estoque_baixo.html', {
        'produtos': produtos
    })