###Proyecto Almacén###
#Integrantes : Dávila Exel , Franco Sorbello , Juan Codilupi
# Versión 1.0  --- 14/6/2018
from Radixsort import *



def Agregar_Estanteria(Almacen,cant_estantes,cant_productos):

  cantidad=cant_estantes*cant_productos

  for i in range(0,cantidad):
    Almacen.append( "{" )


def Agregar_producto(Almacen):

  Producto = str(input("\nNombre del producto: "))

  entrada=input("Cantidad: ")
  while not entrada.isdigit():
    entrada=input("Por favor solo ingrese numeros enteros, vuelva a intentar: ")
  cantidad=int(entrada)

  for j in range(0,cantidad):
    for i in range (len(Almacen)-1):
      if Almacen[i] == "{":
        Almacen[i] = Producto
        break


def imprimir(Almacen,cant_estanterias,cant_estantes,cant_productos):

  for i in range (0,cant_estanterias):
    print("\n\t\t\t\tEstanteria ",i+1)
    contador=1
    for j in range(i*cant_estantes,(i*cant_estantes)+cant_estantes):      
      print("\n\t\tEstante ",contador,end='')
      contador=contador+1      
      for k in range(j*cant_productos,(j*cant_productos)+cant_productos):
        print('',Almacen[k],'',end='')
    print("\n")




print("\t\tBienvenido al Sistema de Stock")
print("\nEn primera instancia vamos a establecer algunos parametros")
cant_estanterias=input("\nCantidad de estanterias del Almacen: ")
while not cant_estanterias.isdigit():
  cant_estanterias=input("\nPor favor solo ingrese numeros enteros, vuelva a intentar: ")
cant_estantes=input("\nCantidad de estantes por estanteria: ")
while not cant_estantes.isdigit():
  cant_estantes=input("\nPor favor solo ingrese numeros enteros, vuelva a intentar: ")
cant_productos=input("\nCantidad de productos por estante: ")
while not cant_productos.isdigit():
  cant_productos=input("\nPor favor solo ingrese numeros enteros, vuelva a intentar: ")

print("Gracias")

cant_estantes=int(cant_estantes)
cant_estanterias=int(cant_estantes)
cant_productos=int(cant_productos)

Almacen=(cant_estanterias*cant_estantes*cant_productos)*["{"]

salir = -1 

while salir != 0 : 
  print("\nMenu")
  print("1-Agregar producto")
  print("2-Ver los productos disponibles")
  print("3-Ordenar lista")
  print("4-Buscar producto")
  print("5-Agregar Estanteria")
  
  

  salir=input("\nIngrese opcion deseada: ")
  while not salir.isdigit():
    salir=input("Por favor solo ingrese numeros enteros, vuelva a intentar: ")
  salir=int(salir)


  if salir == 1 :
    Agregar_producto(Almacen)
    
  elif salir == 2 :
    imprimir(Almacen,cant_estanterias,cant_estantes,cant_productos)

  elif salir == 3 :
    Almacen=RadixSort(Almacen)

  elif salir == 4 :

    print("Hola")
    
  elif salir == 5 :
    Agregar_Estanteria(Almacen,cant_estantes,cant_productos)
    cant_estanterias=cant_estanterias+1
   

  


























