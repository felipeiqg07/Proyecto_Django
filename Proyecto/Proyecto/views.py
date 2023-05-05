
from django.shortcuts import render
from .productos import productos

def mostrar_principal(request):
    return render(request, 'principal.html')

def mostrar_sesion(request):
    return render(request, 'sesion.html')

def mostrar_productos(request):
    resultado = productos
    palabra = ""
    if request.method == 'GET':
        palabra_cliente= request.GET.get('busqueda')
        if palabra_cliente != None:
            palabra = palabra_cliente
            resultado = []
            for variable in productos:
                if palabra_cliente.lower() in variable['nombre'].lower() or palabra_cliente.lower() in variable['detalle'].lower():
                    resultado.append(variable)
            # Logica de busqueda
            pass
    print(request.method)
    context = {
        'titulo':'productitos epicos',
        'lista': resultado,
        'palabra': palabra
    }
    return render(request, 'productos.html', context)