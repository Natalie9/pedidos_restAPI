from django.db import models


# from .forms import ClienteForm
# from django import forms


# Create your models here.


class Produto(models.Model):
    titulo = models.CharField(max_length=50)
    preco = models.FloatField()
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return str(self.titulo)


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()

    # senha = forms.CharField(widget=ClienteForm.PasswordInput)

    def __str__(self):
        return


class Pedido(models.Model):
    data = models.DateField(auto_now=True)
    produtos = models.ManyToManyField(Produto)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str('/'.join(cust.id for cust in self.produtos.all()))

