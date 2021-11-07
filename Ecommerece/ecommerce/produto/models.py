from django.db import models
from .validate import validacao_porcentagem
from django.db.models import F

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.CharField(max_length=400, blank=False, null=False)
    preco = models.DecimalField(max_digits=999, decimal_places=2, blank=False, null=False)
    estoque = models.IntegerField(blank=False, null=False)
    imagem = models.ImageField(upload_to="images/")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    desconto = models.IntegerField(validators=[validacao_porcentagem], blank=True, null=True)
    
    @classmethod
    def atualiza_estoque(self, id):
        produto = Produto.objects.get(id=id)
        produto.estoque = F('estoque') - 1
        produto.save()

    @classmethod
    def preco_liquido(self, id):
        produto = Produto.objects.get(id=id)
        
        return produto.preco - produto.preco * produto.desconto / 100 

    @classmethod
    def return_produto(self, id):
        produto = Produto.objects.get(id=id)

        return produto.nome
        
    def __str__(self):
        return self.nome
