from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from produto.models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = (permissions.IsAdminUser)