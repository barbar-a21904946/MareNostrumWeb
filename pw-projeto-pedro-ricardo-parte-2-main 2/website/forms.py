from django import forms
from django.forms import ModelForm
from .models import Contacto, Comentario, Quizz, Pessoa


class ContactoForm(ModelForm):
    dataNascimento = forms.DateField(label="Data de Nascimento (YYYY-MM-DD)")

    class Meta:
        model = Contacto
        fields = '__all__'


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        opcoes = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ]
        widgets = {
            'clareza': forms.RadioSelect(choices=opcoes),
            'rigor': forms.RadioSelect(choices=opcoes),
            'precisao': forms.RadioSelect(choices=opcoes),
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'
        quantidade = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ]
        widgets = {
            'p8': forms.RadioSelect(choices=quantidade),
            'pontos': forms.HiddenInput(),
        }
        labels = {
            'p1': "Em que ano foi a natação incluida nos Jogos Olímpicos? ",
            'p2': "Qual a cidade onde as mulheres participaram nas provas de natacão nos Jogos Olímpicos pela primera vez? ",
            'p3': "Como se chama o primeiro nadador olímpico portugues? ",
            'p4': "Quantos estilos de natação existem? ",
            'p5': "Indique entre estas opções de estilos qual o verdadeiro ",
            'p6': "Quem lidera na categoria de homens o maior numero de medalhas olímpicas? ",
            'p7': "E na categoria das mulheres? ",
            'p8': "Quantos benifícos da natação fala o nosso site? ",
            'p9': "Quantos tipos de natação existem? ",
            'p10': "Diga de 1 a 10 que nota acha que vai ter neste Quizz ",
        }
