from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import SucursalesFormulario, VehiculoFormulario, VendedorFormulario
from .models import vehiculo, sucursales, vendedor

# Create your views here.

def vehiculos(request):
    
    lista = vehiculo.objects.all()
    return render(request, "vehiculos.html", {"vehiculos": lista})

def sucursal(request):

    listasucursal = sucursales.objects.all()
    return render(request, "sucursales.html", {"sucursales": listasucursal})

def vendedores(request):

    listavendedores = vendedor.objects.all()
    return render(request, "vendedor.html", {"vendedor": listavendedores})

def inicio(request):

    return render(request, "Inicio.html")

def formulario(request):

    if request.method == "POST":
        
        mi_formulario = VehiculoFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            objetos = vehiculo(tipo=data['tipo'], marca=data['marca'], modelo=data['modelo'], usado=data['usado'], 
            puertas=data['puertas'], kilometros=data['kilometros'], año=data['año'], precio=data['precio'])
            objetos.save()
            return redirect('vehiculos')
    else:
        mi_formulario =VehiculoFormulario()

    return render(request, 'Formulario.html', {'mi_formulario':mi_formulario})

def formulario_vendedor(request):

    if request.method == "POST":
        
        mi_formulariovendedor = VendedorFormulario(request.POST)
        if mi_formulariovendedor.is_valid():
            data = mi_formulariovendedor.cleaned_data
            objetos = vendedor(nombre=data['nombre'], email=data['email'], telefono=data['telefono'], atencion=data['atencion'])
            objetos.save()
            return redirect('vendedor')
    else:
        mi_formulariovendedor =VendedorFormulario()

    return render(request, 'Formulario_vendedor.html', {'mi_formulariovendedor':mi_formulariovendedor})

def formulario_sucursal(request):

    if request.method == "POST":
        
        mi_formulariosucursal = SucursalesFormulario(request.POST)
        if mi_formulariosucursal.is_valid():
            data = mi_formulariosucursal.cleaned_data
            objetos = sucursales(nombre=data['nombre'], ubicacion=data['ubicacion'], telefono=data['telefono'])
            objetos.save()
            return redirect('sucursales')
    else:
        mi_formulariosucursal =SucursalesFormulario()

    return render(request, 'Formulario_sucursal.html', {'mi_formulariosucursal':mi_formulariosucursal})

def contacto(request):

    return render(request, "contacto.html")

def agradecimiento(request):

    return render(request, "Agradecimiento.html")

def busqueda_vendedor(request):

    return render(request, "busqueda_vendedor.html")

def buscarV(request):

    if request.GET['nombre']:

        buscar_nombre = request.GET['nombre']
        
        print(buscar_nombre)

        # Esto no esta trayendo solo el telefono del objeto vendedor, esta trayendo el obj entero vendedor
        objeto_vendedor = vendedor.objects.get(nombre = buscar_nombre)

        #Los prints solo estan para que veas q trae
        print(objeto_vendedor.nombre)
        print(objeto_vendedor.telefono)
        print(objeto_vendedor.email)

        # el nombre 'vendedor_contenedor' solo va para usar ese nombre en el html como el obj que tiene los datos
        return render(request, 'resultadobusqueda.html', {'vendedor_contenedor': objeto_vendedor})


    return HttpResponse("No enviaste datos")
    
def busqueda_vehiculos(request):

    return render(request, "busqueda_vehiculos.html")

def buscarVehiculos(request):

    if request.GET['marca']:

        buscar_marca = request.GET['marca']

        lista_obj_vehiculos = vehiculo.objects.filter(marca = buscar_marca)

        return render(request, 'resultadobusquedaVehiculo.html', {'list_vehiculos': lista_obj_vehiculos})


    return HttpResponse("No enviaste datos")

def busqueda_sucursal(request):

    return render(request, "busqueda_sucursal.html")

def buscarSucursal(request):

    if request.GET['nombre']:

        buscar_nombre = request.GET['nombre']
        
        objeto_sucursal = sucursales.objects.get(nombre = buscar_nombre)

        print(objeto_sucursal.nombre)
        print(objeto_sucursal.telefono)

        return render(request, 'resultadobusquedaSucursal.html', {'obj_sucursal': objeto_sucursal})


    return HttpResponse("No enviaste datos")