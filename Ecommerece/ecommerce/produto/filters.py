import django_filters
from .models import Produto

class ProdutoFilter(django_filters.FilterSet):

    nome = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Produto
        fields = ['nome', 'categoria']