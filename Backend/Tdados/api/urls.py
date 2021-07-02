from django.urls import include, path
from rest_framework import routers
from .views import *


urlpatterns = [
    path('dados/adicionar', Dados_adicionar.as_view(), name='adicionar_dados'),
    path('anos', ano_get.as_view(), name='get_anos'),
    path('processar', processar_api.as_view(), name='processar'),
    path('knn', get_knn.as_view(), name='get_knn'),
    # path('get/dados', Buscar, name='Buscar'),

]