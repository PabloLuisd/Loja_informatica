from django.urls import path
from estoque.views.categoria_views import (
    categoria_lista,
    categoria_criar,
    categoria_editar,
    categoria_excluir
)

urlpatterns = [
    path('', categoria_lista, name='categoria_lista'),
    path('nova/', categoria_criar, name='categoria_criar'),
    path('<int:pk>/editar/', categoria_editar, name='categoria_editar'),
    path('<int:pk>/excluir/', categoria_excluir, name='categoria_excluir'),
]