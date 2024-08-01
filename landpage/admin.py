from django.contrib import admin
from .models import FormularioModel

class FormAdmin(admin.ModelAdmin):
    inlines = [FormularioModel]
    list_display = ['nome', 'email', 'telefone', 'nome_empresa', 'segmento', 'funcionarios', 'faturamento']



admin.site.register(FormularioModel, FormAdmin)
