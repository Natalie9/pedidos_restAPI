from rest_framework import serializers
from .models import Produto, Pedido, Cliente


class PedidoSerializer(serializers.ModelSerializer):
    produtos = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), many=True)

    class Meta:
        model = Pedido
        fields = ('id', 'data', 'cliente', 'produtos')


class ProdutoSerializer(serializers.ModelSerializer):
    pedidos = PedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Produto
        fields = ('id', 'titulo', 'preco', 'descricao', 'pedidos')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
