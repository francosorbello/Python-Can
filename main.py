###Proyecto Almacén###
#Integrantes : Dávila Exel , Franco Sorbello , Juan Codilupi
# Versión 1.0

from radix import *


def Agregar_producto(Almacen):
 
  
  for i in range (len(Almacen)-1):

    if Almacen[i] == None:
      
      Almacen[i] = input("Nombre del producto")
      
      return


def imprimir(Almacen):

  for i in range (len(Almacen)-1):
    if Almacen[i]== None:
      continue
    else :
      print(Almacen[i])
    



Almacen=250*[None] ## En cada 5 estanterias hay 5 estantes y cada estante contiene 10 productos



salir = -1 

while salir != 0 : 

  print("Elija la opcion deseada \n")
  print("1-Agregar producto")
  print("2-Ver los productos disponibles")
  print("3-Ordenar lista")
  print("4-Buscar producto")
  
  salir = int(input())


  if salir == 1 :
    Agregar_producto(Almacen)
    
  elif salir == 2 :
    imprimir(Almacen)
  elif salir == 3 :
    radixsort(Almacen)

  


























