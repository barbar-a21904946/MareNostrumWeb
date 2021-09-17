# PAGINA ONDE FAZ OS GRAFICOS MATPLOTLIB
from io import StringIO

from matplotlib import pyplot as plt

from .models import Comentario, Quizz


def comentariosGraficoCircular():
    comentarios = Comentario.objects.all()
    listaKeys = ['Rigor', 'Clareza', 'Precisao']
    rigor = 0
    clareza = 0
    precisao = 0
    listaValues = []
    for coment in comentarios:
        rigor += int(coment.rigor)
        clareza += int(coment.clareza)
        precisao += int(coment.precisao)
    listaValues.append(rigor)
    listaValues.append(clareza)
    listaValues.append(precisao)

    fig = plt.figure()
    plt.pie(listaValues, labels=listaKeys, autopct='%1.0f%%')
    plt.title("Gráfico Critérios de Avaliação")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(4, 2.666)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data


def comentariosGraficoBarras():
    comentarios = Comentario.objects.all()
    listaKeys = ['F. Ler', 'Boa Opti', 'T. Resposta', 'F. Usar']
    ler = 0
    opt = 0
    tem = 0
    usar = 0
    listaValues = []
    for coment in comentarios:
        if coment.facilLer:
            ler += 1
        if coment.optimizacao:
            opt += 1
        if coment.tempoResposta:
            tem += 1
        if coment.facilUsar:
            usar += 1
    listaValues.append(ler)
    listaValues.append(opt)
    listaValues.append(tem)
    listaValues.append(usar)

    fig = plt.figure()
    plt.bar(listaKeys, listaValues)
    plt.title("Gráfico Critérios Considerados")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(4, 2.666)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data


def quizzPessoal(quizz_id):
    quizz = Quizz.objects.get(id=quizz_id)
    listaKeys = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
    listaValues = []
    pontos = 0.0
    if str(quizz.p1) == "1904":
        pontos += 1
        listaValues.append(1)
    elif str(quizz.p1) == "1900":
        pontos += 0.5
        listaValues.append(0.5)
    else:
        listaValues.append(0)

    if quizz.p2 == "Estocolmo":
        pontos += 1
        listaValues.append(1)
    else:
        listaValues.append(0)

    if quizz.p3 == "Mario Marques":
        pontos += 1
        listaValues.append(1)
    elif quizz.p3 == "Mario":
        pontos += 0.5
        listaValues.append(0.5)
    else:
        listaValues.append(0)

    if str(quizz.p4) == "4":
        pontos += 1
        listaValues.append(1)
    else:
        listaValues.append(0)

    if quizz.p5 == "Bruços":
        pontos += 1
        listaValues.append(1)
    else:
        listaValues.append(0)

    if quizz.p6 == "Michael Phelps":
        pontos += 1
        listaValues.append(1)
    elif quizz.p6 == "Michael" or quizz.p6 == "Phelps":
        pontos += 0.5
        listaValues.append(0.5)
    else:
        listaValues.append(0)

    if quizz.p7 == "Jenny Thompson":
        pontos += 1
        listaValues.append(1)
    elif quizz.p7 == "Jenny" or quizz.p7 == "Thompson":
        pontos += 0.5
        listaValues.append(0.5)
    else:
        listaValues.append(0)

    if str(quizz.p8) == "5":
        pontos += 1
        listaValues.append(1)
    else:
        listaValues.append(0)

    if str(quizz.p9) == "2":
        pontos += 1
        listaValues.append(1)
    else:
        listaValues.append(0)

    # p10
    pontos += 1
    listaValues.append(1)

    # grava pontos na base de dados
    quizz.pontos = pontos
    quizz.save()

    fig = plt.figure()
    plt.barh(listaKeys, listaValues)
    plt.title(f"Gráfico Pontos Por Perguntas\n"
              f"Total {quizz.pontos} em 10")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(5, 5)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data


def quizzGrupo(quizz_id):
    quizzes = Quizz.objects.all()
    quizzAtual = Quizz.objects.get(id=quizz_id)
    listaKeys = ["Pontuação Média", "Sua Pontuação"]
    listaValues = []
    mediaGeral = 0.0
    totalUsers = 0.0
    for quizz in quizzes:
        mediaGeral += quizz.pontos
        totalUsers += 1

    mediaGeral = mediaGeral / totalUsers
    listaValues.append(mediaGeral)
    listaValues.append(quizzAtual.pontos)

    fig = plt.figure()
    plt.bar(listaKeys, listaValues)
    plt.title("Gráfico Comparação")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(3, 5)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data
