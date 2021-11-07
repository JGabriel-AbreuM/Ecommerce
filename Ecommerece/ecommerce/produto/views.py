from django.contrib.auth.models import User
from django.db import models
from django.db.models import F, fields
from django.shortcuts import get_object_or_404, render, resolve_url
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from .models import Categoria, Produto
from django.urls import reverse_lazy
from .forms import InsereCategoria, InsereProduto
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import CustomUser
from .filters import ProdutoFilter
from django_filters.views import FilterView

class HomePageView(FilterView):
    """
    Página home do projeto, quando o usuário estiver nela, verá todos os produtos então cadastrados

    Read do CRUD
    """
    model = Produto
    template_name = "home.html"
    context_object_name = "produtos"
    filterset_class = ProdutoFilter


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["preco_liquido"] = Produto.preco_liquido(self.object.id)

        tipo = CustomUser.type_is(CustomUser.id_is(User.objects.all()[0])) == 'CP'

        context["tipo"]  = tipo
        return context


class ConfirmProdutoView(LoginRequiredMixin, DetailView):
    """
    Confirma a compra de um determinado produto
    """
    model = Produto
    template_name = "confirma.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if CustomUser.type_is(CustomUser.id_is(User.objects.all()[0])) == 'CP':
            Produto.atualiza_estoque(self.object.id)
            context["invalido"] = False

        else:
            context["invalido"] = True
        
        return context

class CarrinhoView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        response = render(request, 'carrinho.html', context)

        ids = request.COOKIES["produtos"]
        elements = []
        for id in ids:
            if id == ',':
                continue

            elements.append(int(id))

        products = []
        for e in elements:
            products.append(Produto.return_produto(e))
        
        context["elementos"] = products    
        response = render(request, 'carrinho.html', context)
        return response

class ConfirmCarrinhoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'confirma_carrinho.html')
