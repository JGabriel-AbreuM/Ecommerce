from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from produto.models import Produto

class ProdutoSerializer(ModelSerializer):
    """
    Serializer de minha api
    """
    class Meta:
        model = Produto
        fields = ("id", "nome", "descricao", "preco", "categoria")