from django.shortcuts import render, redirect, get_object_or_404
from ..models import Categoria
from ..forms import CategoriaForm


def categoria_lista(request):
    categorias = Categoria.objects.all()

    return render(request, 'estoque/categoria_lista.html', {
        'categorias': categorias
    })


def categoria_criar(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('estoque:categoria_lista')

    return render(request, 'estoque/formulario.html', {
        'form': form,
        'titulo': 'Nova Categoria'
    })


def categoria_editar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('estoque:categoria_lista')

    return render(request, 'estoque/formulario.html', {
        'form': form,
        'titulo': 'Editar Categoria'
    })


def categoria_excluir(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        categoria.delete()
        return redirect('estoque:categoria_lista')

    return render(request, 'estoque/confirmar_exclusao.html', {
        'objeto': categoria,
        'titulo': 'Excluir Categoria'
    })