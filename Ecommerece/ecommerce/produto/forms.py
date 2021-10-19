from django import forms
from django.db import models
from django.db.models import fields
from .models import Categoria, Produto

class InsereCategoria(forms.ModelForm):
    """
    Formulário para inserção de uma determinada categoria.
    """
    class Meta:
        model = Categoria

        fields = [
            "nome"
        ]

class InsereProduto(forms.ModelForm):
    """
    Formulário para adição de um produto.
    """
    class Meta:
        model = Produto

        fields = [
            "nome",
            "descricao",
            "preco",
            "estoque",
            "imagem",
            "categoria",
        ]

