from django.urls import path
from ..views.movimentacao_views import (
    movimentacao_lista,
    movimentacao_criar
)

urlpatterns = [
    path('', movimentacao_lista, name='movimentacao_lista'),
    path('nova/', movimentacao_criar, name='movimentacao_criar'),
]