from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    sexo ='m'
    nome = "Joaquina"
    lista = [{'nome':'William', 'sexo':'m'},
             {'nome':'Carlos', 'sexo':'m'},
             {'nome':'Letícia', 'sexo':'f'},
             {'nome':'Maria', 'sexo':'f'},
        ]
    return render(request,'index.html', {'lista':lista,'nome': nome, 'sexo': sexo})
