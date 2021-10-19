from django.db import router
from django.urls import path
from .views import HomePageView, AddCategoriaView, AddProdutoView, DeleteProdutoView, UpdateProdutoView, DetailProdutoView, ConfirmProdutoView


app_name = "produto"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("add_categoria/", AddCategoriaView.as_view(), name="categoria"),
    path("add_produto/", AddProdutoView.as_view(), name="produto"),
    path("exclui/<pk>", DeleteProdutoView.as_view(), name="delete"),
    path("atualiza/<pk>", UpdateProdutoView.as_view(), name="atualiza"),
    path("produto/<pk>", DetailProdutoView.as_view(), name="detalhe"),
    path("confirma/<pk>", ConfirmProdutoView.as_view(), name="confirma")
]