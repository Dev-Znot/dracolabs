from django import forms

from .models import FormularioModel

class Formulario(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Seu nome", "id":"nome"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Seu e-mail", "id":"email"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Telefone com DDD", "id":"telefone"}))
    nome_empresa = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Nome da empresa", "id":"nome_empresa"}))
    segmento = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Seu segmento?", "id":""}))
    funcionarios = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Quantos funcionarios?", "id":""}))
    faturamento = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Faturamento mensal?", "id":""}))

    class Meta:
        model = FormularioModel
        fields = ['nome', 'email', 'telefone', 'nome_empresa', 'segmento', 'funcionarios', 'faturamento']