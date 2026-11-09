from django import forms
from .models import Categoria, Fornecedor, Produto, MovimentacaoEstoque

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome','descricao']

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome','cnpj','telefone','email']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','descricao','preco','quantidade_estoque','categoria','fornecedor']
    def clean_preco(self):
        valor = self.cleaned_data['preco']
        if valor < 0: raise forms.ValidationError('O preço não pode ser negativo.')
        return valor

class MovimentacaoEstoqueForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ['produto','tipo','quantidade','observacao']
    def clean_quantidade(self):
        valor = self.cleaned_data['quantidade']
        if valor <= 0: raise forms.ValidationError('A quantidade deve ser maior que zero.')
        return valor
