from django.contrib import admin
from .models import FormularioModel

class FormAdmin(admin.ModelAdmin):
    inlines = [FormularioModel]
    list_display = ['nome', 'telefone']



admin.site.register(FormularioModel, FormAdmin)
