from django.urls import path
from estoque.views.produto_views import (
    produto_lista,
    produto_criar,
    produto_editar,
    produto_excluir,
    estoque_baixo
)

urlpatterns = [
    path('', produto_lista, name='produto_lista'),
    path('novo/', produto_criar, name='produto_criar'),
    path('estoque-baixo/', estoque_baixo, name='estoque_baixo'),
    path('<int:pk>/editar/', produto_editar, name='produto_editar'),
    path('<int:pk>/excluir/', produto_excluir, name='produto_excluir'),
]