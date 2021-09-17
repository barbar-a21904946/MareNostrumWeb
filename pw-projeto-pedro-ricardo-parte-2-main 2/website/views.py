import time

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .matplot import comentariosGraficoCircular, comentariosGraficoBarras, quizzPessoal, quizzGrupo
from .forms import ContactoForm, ComentarioForm, QuizzForm

# Create your views here.
from .models import Contacto, Pessoa


def home_page_view(request):
    return render(request, 'website/index.html')


def seccoes(request):
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 12))

    data = []
    for i in range(start, end + 1):
        data.append(f"{i}")

    time.sleep(0.5)

    return JsonResponse({
        "seccoes": data
    })


def about_page_view(request):
    return render(request, 'website/about.html')


def benificios_page_view(request):
    return render(request, 'website/benificios.html')


def comentarios_page_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        comentario = form.save()
        Pessoa.objects.get_or_create(nome=comentario.nome)
        pessoa = Pessoa.objects.get(nome=comentario.nome)
        pessoa.comentario = comentario
        pessoa.save()
        context = {
            'form': form,
            'graphCir': comentariosGraficoCircular(),
            'graphBar': comentariosGraficoBarras()
        }
    else:
        context = {'form': form}

    return render(request, 'website/comentarios.html', context)


def estilos_page_view(request):
    return render(request, 'website/estilos.html')


def galeria_page_view(request):
    return render(request, 'website/galeria.html')


def provas_page_view(request):
    return render(request, 'website/provas.html')


def contacto_page_view(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        contacto = form.save()
        Pessoa.objects.get_or_create(nome=contacto.nome)
        pessoa = Pessoa.objects.get(nome=contacto.nome)
        pessoa.contacto = contacto
        pessoa.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {'form': form}

    return render(request, 'website/contacto.html', context)


def contactoLista_page_view(request):
    context = {'contactos': sorted(Contacto.objects.all(), key=lambda objeto: objeto.id)}
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('website:login'))

    return render(request, 'website/contactoLista.html', context)


def contactoEditar_page_view(request, contacto_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('website:login'))

    contacto = Contacto.objects.get(pk=contacto_id)
    form = ContactoForm(request.POST or None, instance=contacto)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contactoLista'))

    context = {'form': form, 'contacto_id': contacto_id}
    return render(request, 'website/contactoEditar.html', context)


def contactoApaga_page_view(request, contacto_id):
    Contacto.objects.get(pk=contacto_id).delete()
    return HttpResponseRedirect(reverse('website:contactoLista'))


def quizz_page_view(request):
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        quizz = form.save()
        Pessoa.objects.get_or_create(nome=quizz.nome)
        pessoa = Pessoa.objects.get(nome=quizz.nome)
        pessoa.quizz = quizz
        pessoa.save()
        return HttpResponseRedirect(reverse('website:quizzResult', args=(quizz.id,)))

    context = {
        'form': form,
    }
    return render(request, 'website/quizz.html', context)


def quizzResult_page_view(request, id):
    context = {
        'graphPessoal': quizzPessoal(id),
        'graphGrupo': quizzGrupo(id),
    }
    return render(request, 'website/quizzResult.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return contactoLista_page_view(request)
        else:
            return render(request, 'website/login.html', {
                'Mensagem': "Credenciais Inválidas"
            })
    return render(request, 'website/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'website/index.html', {
        'Mensagem': 'Terminou Sessão'})
