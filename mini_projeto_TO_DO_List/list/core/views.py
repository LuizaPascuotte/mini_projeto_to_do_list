from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def cadastro(request):
    return HttpResponse("Cadastro aqui ó")