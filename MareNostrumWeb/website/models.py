from django.db import models


class Pessoa(models.Model):
    nome= models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Praias(models.Model):
    nome=models.CharField(max_length=100,unique=True)
    pessoas=models.ManyToManyField("Pessoa",related_name="praias")

    def __str__(self):
        return self.nome