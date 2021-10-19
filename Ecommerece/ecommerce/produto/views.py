from django.db import models
from django.db.models import F
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from .models import Categoria, Produto
from django.urls import reverse_lazy
from .forms import InsereCategoria, InsereProduto
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(ListView):
    """
    Página home do projeto, quando o usuário estiver nela, verá todos os produtos então cadastrados

    Read do CRUD
    """
    model = Produto
    template_name = "home.html"
    context_object_name = "produtos"


class AddCategoriaView(LoginRequiredMixin, CreateView):
    """
    Tornará possível a criação de uma nova categoria, será necessário estar logado para cadastrar novas categorias

    Create do CRUD
    """
    template_name = "cria_categoria.html"
    model = Categoria
    form_class = InsereCategoria
    success_url = reverse_lazy("produto:home")

class AddProdutoView(LoginRequiredMixin, CreateView):
    """
    Tornará possível o cadastro de uma novo produto, será necessário estar logado para cadastrar novos produtos

    Create do CRUD
    """
    template_name = "cria_produto.html"
    model = Produto
    form_class = InsereProduto
    success_url = reverse_lazy("produto:home")

class UpdateProdutoView(LoginRequiredMixin, UpdateView):
    """
    Realizará a atualização de um determinado produto, Login Necessário

    Update do CRUD
    """
    template_name = "atualiza.html"
    model = Produto
    context_object_name = "produto"
    fields = "__all__"
    success_url = reverse_lazy("produto:home")

class DeleteProdutoView(LoginRequiredMixin, DeleteView):
    """
    Apagamento de um determinado produto, Login Necessário

    Delete do CRUD
    """
    template_name = "delete.html"
    model = Produto
    context_object_name = "produto"
    success_url = reverse_lazy("produto:home")

class DetailProdutoView(LoginRequiredMixin, DetailView):
    """
    Realizará a compra de um determinado produto.    
    """
    model = Produto
    template_name = "compra.html"
    context_object_name = "produto"

class ConfirmProdutoView(LoginRequiredMixin, UpdateView):
    """
    Confirma a compra de um determinado produto
    """
    model = Produto
    template_name = "confirma.html"
