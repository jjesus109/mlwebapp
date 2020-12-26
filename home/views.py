
from django.shortcuts import render


def index(request):
    # request = {"hola":"jeje"}
    context = {}
    return render(request,"index.html",context)