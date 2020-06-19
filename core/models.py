from django.db import models


# from .forms import ClienteForm
# from django import forms


# Create your models here.


class Produto(models.Model):
    titulo = models.CharField(max_length=50)
    preco = models.FloatField()
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nome



class Pedido(models.Model):
    data = models.DateField(auto_now=True)
    produtos = models.ManyToManyField(Produto, related_name="book_list", blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str('Pedido ' + str(self.id) + ' de ' + self.cliente.nome)
    
    

    

