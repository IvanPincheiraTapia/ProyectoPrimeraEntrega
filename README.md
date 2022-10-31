# ProyectoPrimeraEntrega
Proyecto de venta de vehículos y administración de concesionaria
# ProyectoFinalVehiculos
Proyecto entrega parcial de vehiculos

El proyecto conciste en ofrecer una lista de venta de vehiculos (/concesionaria/vehiculos/), donde el usuario
podra emitir un leads de contacto, tambien habrá una vista de sucursales (/concesionaria/sucursales/) donde se podrá acceder a los lugares de compra, y finalmente una intranet de la empresa, donde la vista del ejecutivo comercial podrá ejecutar una serie de funcionalidades (/concesionaria/vendedor/) poara buscar vehiculos, sucursales o ejecutivos, asi tambien agregar nuevos vehiculos de ventas, nuevas sucursales y ejecutivos.

La app parte con: /concesionaria/inicio/

App venta vehiculos
"Una Aplicacion donde vender vehiculos"


###### Urls Explcados en orden de posicion ######

path('vehiculos/', vehiculos, name="vehiculos")
"Muestra la lista de vehiculos en una tabla"

path('vendedor/', vendedores, name="vendedor")
"""
"Es la vista de administrador del sitio"
"Muestra la lista de vendedores "
"Tiene los botones tanto para agregar como buscar vehiculos, vendedores y sucursales"

"""

path('sucursales/', sucursal, name="sucursales")
"Muestra la lista de sucursales"

path('Inicio/', inicio, name="inicio")
"Inicio con botones a las lista vehiculos, sucursales y vendedores"

path('Formulario/', formulario, name="Formulario")
"Formulario para agregar Vehiculos"

path('contacto/', contacto, name="contacto")
"Formulario de contacto"

path('agradecimiento/', agradecimiento, name="Agradecimiento")
"Se carga al terminar el Formulario de contacto mostrando gracias"

path('busqueda_vendedor/', busqueda_vendedor, name="busqueda_vendedor")
"Formulario de busqueda de vendedor por nombre"

path('busqueda_vehiculos/', busqueda_vehiculos, name="busqueda_vehiculos")
"Formulario de busqueda de vehiculos por marca"

path('busqueda_sucursal/', busqueda_sucursal, name="busqueda_sucursal")
"Formulario de busqueda de Sucursal por nombre"

path('buscar/', buscarV, name="busquedaV"),
"Se carga al terminar el Formulario de Vendedor mostrando teléfono de vendedor"

path('buscarVehiculos/', buscarVehiculos, name="busquedaVehiculo")
"Se carga al terminar el Formulario de Vehiculos mostrando Cada Vehiculo con sus datos de la Marca puesta"

path('Formulario_vendedor/', formulario_vendedor, name="Formulario_vendedor")
"Formulario para agregar Vendedores"

path('Formulario_sucursal/', formulario_sucursal, name="Formulario_sucursal")
"Formulario para agregar Surcursales"


######### Modelos #########

class vehiculo(models.Model): Vehiculo

    tipo = tipo del vehiculo
    marca = marca del vehiculo
    modelo = modelo del vehiculo
    puertas = numero de puertas
    usado = usado / semi-usado / nuevo
    kilometros = Cuantos kilometros de uso tiene
    año = Cuantos años de uso tiene
    precio = precio del vehiculo

class vendedor(models.Model): Ejecutivo

    nombre = nombre del ejecutivo
    email = email del ejecutivo
    telefono = numero de contacto del ejecutivo
    atencion = Division de trabajo

class sucursales(models.Model): Sucursal

    nombre = nombre de la Sucursal
    ubicacion = calle de la Sucursal
    telefono = numero de contacto de la Sucursal
