from django.contrib import admin

# Register your models here.
from .models import Pedido, Produto, Cliente




admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Cliente)

admin.site.site_header = "Ifude"