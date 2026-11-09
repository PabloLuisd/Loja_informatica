from django.urls import path
from ..views.fornecedor_views import (
    fornecedor_lista,
    fornecedor_criar,
    fornecedor_editar,
    fornecedor_excluir
)

urlpatterns = [
    path('', fornecedor_lista, name='fornecedor_lista'),
    path('novo/', fornecedor_criar, name='fornecedor_criar'),
    path('<int:pk>/editar/', fornecedor_editar, name='fornecedor_editar'),
    path('<int:pk>/excluir/', fornecedor_excluir, name='fornecedor_excluir'),
]