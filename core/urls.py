# Importamos a função index() definida no arquivo views.py
from core.views import IndexViewSet

from django.urls import path, include

app_name = 'core'

# urlpatterns a lista de roteamentos de URLs para funções/Views
urlpatterns = [
    # GET /
    path('', IndexViewSet.as_view()),
]
