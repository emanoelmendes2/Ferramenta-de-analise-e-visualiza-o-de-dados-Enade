from django.urls import include, path
from rest_framework import routers


from .views import *
urlpatterns = [
    path('dados/adicionar', Dados_adicionar.as_view(), name='adicionar_dados'),

]