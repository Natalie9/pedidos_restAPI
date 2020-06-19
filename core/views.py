from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView
from .models import Produto, Cliente, Pedido
from .serializer import ProdutoSerializer, PedidoSerializer, ClienteSerializer
# Create your views here.

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class IndexViewSet(ListView):
    template_name = "index.html"
    model = Pedido
    context_object_name = "clientes"