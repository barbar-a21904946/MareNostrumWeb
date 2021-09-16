#  hello/urls.py
from django.urls import path
from django.shortcuts import render
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('historia', views.historia_page_view, name='historia'),
    path('explorar', views.explorar_page_view, name='explorar')
]
