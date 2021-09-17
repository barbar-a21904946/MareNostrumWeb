from django.db import models


# Create your models here.

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, default="", verbose_name="O seu Nome ")
    email = models.EmailField()
    telefone = models.CharField(max_length=17, blank=True)
    dataNascimento = models.DateField()
    dataCriacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, default="", verbose_name="O seu Nome ")
    clareza = models.CharField(max_length=10, default=3)
    rigor = models.CharField(max_length=10, default=3)
    precisao = models.CharField(max_length=10, default=3)
    optimizacao = models.BooleanField(verbose_name="Boa optimização para telemóvel", default=False)
    tempoResposta = models.BooleanField(verbose_name="Tempo de resposta do Website", default=False)
    facilUsar = models.BooleanField(verbose_name="Fácil de Usar", default=False)
    facilLer = models.BooleanField(verbose_name="Fácil de Ler", default=False)
    feedBack = models.TextField(default="")

    def __str__(self):
        return str(self.id)


class Quizz(models.Model):
    id = models.AutoField(primary_key=True)
    pontos = models.FloatField(default=0.0)
    nome = models.CharField(max_length=30, default="", verbose_name="O seu Nome ")
    p1 = models.IntegerField(default=0)
    p2 = models.CharField(max_length=40, default="")
    p3 = models.CharField(max_length=40, default="")
    quantidade = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    p4 = models.IntegerField(choices=quantidade, default=0)
    opcoes = [
        ("Braços", "Braços"),
        ("Bruços", "Bruços"),
        ("Pernas", "Pernas"),
    ]
    p5 = models.CharField(choices=opcoes, default="", max_length=40)
    p6 = models.CharField(max_length=40, default="")
    p7 = models.CharField(max_length=40, default="")
    p8 = models.IntegerField(default=0)
    p9 = models.IntegerField(default=0, choices=quantidade)
    opcoesNota = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    ]
    p10 = models.IntegerField(default=0, choices=opcoesNota)

    def __str__(self):
        return str(self.id)


# REQUISITO DA FOREIGN KEY
class Pessoa(models.Model):
    nome = models.CharField(max_length=30, default="", verbose_name="O seu Nome ")
    contacto = models.ForeignKey(Contacto, on_delete=models.SET_NULL, blank=True, null=True)
    comentario = models.ForeignKey(Comentario, on_delete=models.SET_NULL, blank=True, null=True)
    quizz = models.ForeignKey(Quizz, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nome
