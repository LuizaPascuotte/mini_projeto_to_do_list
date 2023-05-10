from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def cadastro(request):
    return render(request, "cadastro.html")