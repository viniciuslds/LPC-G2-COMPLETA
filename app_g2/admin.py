from django.contrib import admin
from .models import *

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Veiculos)
class VeiculosAdmin(admin.ModelAdmin):
    pass

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Solicitacoes)
class SolicitacoesAdmin(admin.ModelAdmin):
    pass


