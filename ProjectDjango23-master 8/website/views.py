from django.shortcuts import render

# Create your views here.
#  hello/views.py

from django.shortcuts import render
import datetime


def home_page_view(request):
    lista = ["HTML", "CSS", "Python", "Django"]
    context = {
        'agora': datetime.datetime.now(),
        'lista': lista,
    }
    return render(request, 'website/home.html')

def explorar_page_view(request):
    return render(request, 'website/explorar.html')

def historia_page_view(request):
    return render(request, 'website/historia.html')
