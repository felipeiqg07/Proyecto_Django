from django.shortcuts import render


def mostrar_principal(request):
    return render(request, 'principal.html')

def mostrar_sesion(request):
    return render(request, 'sesion.html')