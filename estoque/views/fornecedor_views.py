from django.shortcuts import render, redirect, get_object_or_404
from ..models import Fornecedor
from ..forms import FornecedorForm


def fornecedor_lista(request):
    fornecedores = Fornecedor.objects.all()

    return render(request, 'estoque/fornecedor_lista.html', {
        'fornecedores': fornecedores
    })


def fornecedor_criar(request):
    form = FornecedorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('estoque:fornecedor_lista')

    return render(request, 'estoque/formulario.html', {
        'form': form,
        'titulo': 'Novo Fornecedor'
    })


def fornecedor_editar(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    form = FornecedorForm(request.POST or None, instance=fornecedor)

    if form.is_valid():
        form.save()
        return redirect('estoque:fornecedor_lista')

    return render(request, 'estoque/formulario.html', {
        'form': form,
        'titulo': 'Editar Fornecedor'
    })


def fornecedor_excluir(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)

    if request.method == 'POST':
        fornecedor.delete()
        return redirect('estoque:fornecedor_lista')

    return render(request, 'estoque/confirmar_exclusao.html', {
        'objeto': fornecedor,
        'titulo': 'Excluir Fornecedor'
    })