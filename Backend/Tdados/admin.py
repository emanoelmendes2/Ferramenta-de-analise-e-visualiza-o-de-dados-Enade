from django.contrib import admin
from .models import *

@admin.register(Dados)
class DadosAdmin(admin.ModelAdmin):
    pass

@admin.register(Enade)
class EnadeAdmin(admin.ModelAdmin):
    pass

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    pass