from django.db import models

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

    def __str__(self):
        return self.nome