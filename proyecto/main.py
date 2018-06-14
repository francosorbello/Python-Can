###Proyecto Almacén###
#Integrantes : Dávila Exel , Franco Sorbello , Juan Codilupi
# Versión 1.0

from radix import *

def hash_insert(pos,producto,tabla):
  hash_table[producto]=pos
  return hash_table

def hash_search(producto,tabla):
  return tabla[producto]

def hash_delete(producto,tabla):
  del tabla[producto]
  return tabla


def Agregar_producto(Almacen,hash_table):
 
  for i in range (len(Almacen)-1):

    if Almacen[i] == None:
      
      Almacen[i] = input("Nombre del producto: ")
      hash_insert(i,Almacen[i],hash_table)
      print("...")
      print("Producto agregado.")
      print(" ")
      return


def imprimir(Almacen):
  print("Estantería: 1")
   print("Estante: 1")
   estante=1
   estanteria_aux=0
   estante_aux=0
   
  for i in range (len(Almacen)-1):
    if estante_aux==aux*4:
      print("Estantería: ",estanteria)
      print("Estante: ",estante)
      
    if Almacen[i] != None:
      print("[",Almacen[i],"]")
      

Almacen=250*[None] ## En cada 5 estanterias hay 5 estantes y cada estante contiene 10 productos

hash_table={} 

salir = -1 

while salir != 0 : 

  print("Elija la opcion deseada \n")
  print("1-Agregar producto")
  print("2-Ver los productos disponibles")
  print("3-Ordenar lista")
  print("4-Buscar producto")
  
  salir = int(input())


  if salir == 1 :
    Agregar_producto(Almacen,hash_table)
    
  elif salir == 2 :
    imprimir(Almacen)
  elif salir == 3 :
    radixsort(Almacen)
    hash_table={}#reseteo la tabla de hash
    #vuelvo a hashear los elementos
    for i in range(0,len):
      hash_insert(i,Almacen[i],hash_table)

  #elif salir == 4:
    

  


























