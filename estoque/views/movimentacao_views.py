from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.db.models import F
from ..models import Produto, MovimentacaoEstoque
from ..forms import MovimentacaoEstoqueForm


def movimentacao_lista(request):
    movimentacoes = MovimentacaoEstoque.objects.select_related(
        'produto'
    ).all()

    return render(request, 'estoque/movimentacao_lista.html', {
        'movimentacoes': movimentacoes
    })


@transaction.atomic
def movimentacao_criar(request):
    form = MovimentacaoEstoqueForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        movimentacao = form.save(commit=False)

        produto = Produto.objects.select_for_update().get(
            pk=movimentacao.produto.pk
        )

        quantidade = movimentacao.quantidade

        if movimentacao.tipo == MovimentacaoEstoque.ENTRADA:
            Produto.objects.filter(pk=produto.pk).update(
                quantidade_estoque=F('quantidade_estoque') + quantidade
            )

        elif movimentacao.tipo == MovimentacaoEstoque.SAIDA:
            if quantidade > produto.quantidade_estoque:
                form.add_error(
                    'quantidade',
                    'Quantidade maior que o estoque disponível.'
                )

                return render(request, 'estoque/formulario.html', {
                    'form': form,
                    'titulo': 'Nova Movimentação'
                })

            Produto.objects.filter(pk=produto.pk).update(
                quantidade_estoque=F('quantidade_estoque') - quantidade
            )

        movimentacao.save()

        messages.success(
            request,
            'Movimentação registrada com sucesso!'
        )

        return redirect('estoque:movimentacao_lista')

    return render(request, 'estoque/formulario.html', {
        'form': form,
        'titulo': 'Nova Movimentação'
    })