from django.shortcuts import render
from .productos import productos

def mostrar_principal(request):
    return render(request, 'principal.html')

def mostrar_sesion(request):
    return render(request, 'sesion.html')

def mostrar_productos(request):
    context = {
        'titulo':'productitos epicos',
        'lista': productos,
    }
    return render(request, 'productos.html', context)