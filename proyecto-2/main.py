###Proyecto Almacén###
#Integrantes : Dávila Exel , Franco Sorbello , Juan Codilupi
# Versión 1.0  --- 14/6/2018
from Radixsort import *
from hash import *


#####DEVOLUCION DE POSICION####



def devuelvo_posicion(x,cant_estantes,cant_productos,n):
    #devuelve la estanteria y el estante en el que se encuentra
    #un producto basado en su posicion en la lista
    if x != None:
        estanteria=0
        aux=cant_productos*cant_estantes
        for i in range(0,n+1,aux):
            if i>=x :
                print("Estanteria ",estanteria)
                break 
            estanteria+=1
        estante=0
        for a in range((estanteria-1)*aux,i+1,cant_productos):
            #reduzco la búsqueda a la estantería donde esta el producto
            if a>=x:
                print("Estante ",estante)
                break
            estante+=1


#####AGREGAR ESTANTERIA#####


def Agregar_Estanteria(Almacen,cant_estantes,cant_productos):

  cantidad=cant_estantes*cant_productos

  for i in range(0,cantidad):
    Almacen.append( "{" )


####AGREGAR PRODUCTO#####


def Agregar_producto(Almacen,tabla):

  Producto = str(input("\nNombre del producto: "))

  entrada=input("Cantidad: ")
  while not entrada.isdigit():
    entrada=input("Por favor solo ingrese numeros enteros, vuelva a intentar: ")
  cantidad=int(entrada)
  if cantidad > len(Almacen):
    print("\nNo hay suficiente espacio en el almacen!!! Agregue una Estanteria antes de continuar")
    return    


  else:
    contador=0
    for i in range (len(Almacen)):
        if Almacen[i] == "{":
          contador=contador+1

    if cantidad>contador:
      print("\nNo hay suficiente espacio para agregar esa cantidad de productos,reduzca la cantidad o agregue una estanterias antes de continuar")
      return
    else:
      for j in range(0,cantidad):
        for i in range (len(Almacen)):
          if Almacen[i] == "{":
            Almacen[i] = Producto
            hash_insert(i,Producto,tabla)
            break


#IMPRIME EL ALMACEN####


def imprimir(Almacen,cant_estanterias,cant_estantes,cant_productos):

  for i in range (0,cant_estanterias):
    print("\n\t\t\t\tEstanteria ",i+1)
    contador=1
    for j in range(i*cant_estantes,(i*cant_estantes)+cant_estantes):      
      print("\n\t\tEstante ",contador,end=':')
      contador=contador+1      
      for k in range(j*cant_productos,(j*cant_productos)+cant_productos):
        if Almacen[k] == "{":
          print('',"VACIO",'',end='')

        else:
          print('',Almacen[k],'',end='')
    print("\n")

######COMIENZO#####


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
cant_estanterias=int(cant_estanterias)
cant_productos=int(cant_productos)

aux=cant_estanterias*cant_estantes*cant_productos
Almacen=aux*["{"]
hash_table={}

salir = -1 

############MENU#######


while salir != 0 : 
  print("\nMenu")
  print("1-Agregar producto")
  print("2-Ver los productos disponibles")
  print("3-Ordenar lista")
  print("4-Buscar producto")
  print("5-Agregar Estanteria")
  print("6-Eliminar producto")
  print("7-Terminar programa")
  

  salir=input("\nIngrese opcion deseada: ")
  while not salir.isdigit():
    salir=input("Por favor solo ingrese numeros enteros, vuelva a intentar: ")
  salir=int(salir)


  if salir == 1 :
    Agregar_producto(Almacen,hash_table)
    
  elif salir == 2 :
    imprimir(Almacen,cant_estanterias,cant_estantes,cant_productos)

  elif salir == 3 :
    Almacen=RadixSort(Almacen)
    hash_table={} #reinicio la hash hash_table
    for i in range(0,len(Almacen)):
        #rehasheo todos los elementos
        hash_insert(i,Almacen[i],hash_table)
  elif salir == 4 :
    
    producto=input("Ingrese el producto que está buscando: ")
    aux=hash_search(producto,hash_table)
    devuelvo_posicion(aux,cant_estantes,cant_productos,len(Almacen))
    
  elif salir == 5 :
    Agregar_Estanteria(Almacen,cant_estantes,cant_productos)
    cant_estanterias=cant_estanterias+1
    print('\nSe agrego una nueva estanteria,tiene',cant_estantes*cant_productos,'espacios mas disponibles el almacen ahora tiene',len(Almacen),'espacios en total')
  
  elif salir == 6:
      producto=input("Ingrese el producto que quiere eliminar: ")
      #busco la posicion del producto
      pos=hash_search(producto,hash_table)
      if pos != None:
        aux=Almacen[pos]
        Almacen[pos]="{" #reemplazo el producto por "{"
        hash_delete(aux,hash_table) #borro el producto de la hash table
  elif salir == 7:
    salir=0
  else:
    print("Ingrese un número válido")