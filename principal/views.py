from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def registro_alumnos(request):
    return render(request, "registro_alumnos.html")