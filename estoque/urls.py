from django.urls import path, include
from .views.home_views import dashboard

app_name = 'estoque'

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path(
        'categorias/',
        include('estoque.urls_configs.categoria_urls')
    ),

    path(
        'fornecedores/',
        include('estoque.urls_configs.fornecedor_urls')
    ),

    path(
        'produtos/',
        include('estoque.urls_configs.produto_urls')
    ),

    path(
        'movimentacoes/',
        include('estoque.urls_configs.movimentacao_urls')
    ),
]