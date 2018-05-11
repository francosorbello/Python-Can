from arboless import *
from algo1 import *

def delete(bt,key):
    deletenode=access(bt,key)
    print("debug:",deletenode.key)
    if deletenode.leftnode == None and deletenode.rightnode == None:
        deletenode.parent=None
        return
    elif deletenode.leftnode != None:
        aux=deletenode.leftnode.value
        mayor=buscamax(deletenode.leftnode,aux)
        print("debug mayor:",mayor)
        deleting(bt,mayor,deletenode)
        return
    else:
        aux=deletenode.rightnode.value
        menor=buscamin(deletenode.rightnode,aux)
        #print("debug menor:",menor)
        deleting(bt,menor,deletenode)
        return

def buscamax(deletenode,aux):
  if deletenode != None:
    if deletenode.value >= aux:
      aux=deletenode.value
    buscamin(deletenode.rightnode,aux)
  return aux

def buscamin(deletenode,aux):
  if deletenode != None:
    if deletenode.value <= aux:
      aux=deletenode.value
    buscamin(deletenode.rightnode,aux)
  return aux

def deleting(bt,minomax,deletenode):
    aux=deletenode.rightnode.value
    deletenodeaux=access(bt,minomax) #en esta variable auxiliar guardo el nodo que reemplaza al que borro
    deletenode.value=deletenodeaux.value #reemplazo los valores
    deletenode.key=deletenodeaux.key #reemplazo la key
    deletenodeaux.parent=None

class node:
  value=None
  nextnode=None

class LinkedList:
  head=None

l=LinkedList()

class btree:
  root=None

class btreenode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None
  
rootnobt=btreenode()
rootnobt.key=6
rootnobt.value=6
bt=btree()
bt.root=rootnobt

insert(bt,4,4)
insert(bt,3,3)
insert(bt,5,5)
insert(bt,8,8)
insert(bt,9,9)
insert(bt,7,7)

#n=input_int("Inserte cantidad de elementos:")

#for a in range(0,n):
  #key=input_int("Inserte key")
  #value=input_int("Inserte valor")
  #insert(bt,key,value)
amplitud(rootnobt)
llave=int(input(("Ingrese la key del nodo a eliminar:")))
preorden(bt)
delete(bt,llave)
print("")
preorden(bt)