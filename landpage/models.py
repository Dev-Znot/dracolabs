from django.db import models

class FormularioModel(models.Model):
    nome = models.CharField(max_length=22)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=14)
    nome_empresa = models.CharField(max_length=22)
    segmento = models.CharField(max_length=22)
    funcionarios = models.IntegerField()
    faturamento = models.CharField(max_length=22)


    def __str__(self):
        return self.nome
    


