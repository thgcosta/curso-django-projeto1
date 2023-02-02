from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Thiago Costa',
    })


def sobre(request):
    return HttpResponse('Sobre')


def contato(request):
    return HttpResponse('contato')
