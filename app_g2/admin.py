from django.contrib import admin
from .models import *

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass
