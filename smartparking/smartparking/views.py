from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    var = "Variavel no HTML"
    return render(request,'index.html', {'var': var})
