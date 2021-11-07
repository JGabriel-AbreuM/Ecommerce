from django import http
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics, serializers
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from produto.models import Produto
from .serializers import ProdutoSerializer
from django.contrib.auth import login
from django.contrib.auth.models import User

class ProdutoViewSet(ModelViewSet):
    """
    ViewSet de minha API, apenas usuarios adminstradores terão acesso a esse
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAdminUser]

