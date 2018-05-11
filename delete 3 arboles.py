from arboless import *
from algo1 import *

def buscamax(nodoaux,comparo):
    if nodoaux != None:
        if nodoaux.key<comparo:
            return nodoaux.value
        else:
            if nodoaux.leftnode!=None:
                aux1=buscamax(nodoaux.leftnode,comparo)
                if aux1<=comparo and nodoaux == None:
                  return aux1
            if nodoaux.rightnode != None:
                aux1=buscamax(nodoaux.rightnode,comparo)
                if aux1<=comparo:
                  return aux1
            else:
                return comparo

def buscamin(nodoaux,comparo):
    if nodoaux != None:
        if nodoaux.key>comparo:
            return nodoaux.value
        else:
            if nodoaux.leftnode!=None:
                aux1=buscamin(nodoaux.leftnode,comparo)
                if aux1>comparo and nodoaux.leftnode == None:
                  return aux1
            elif nodoaux.rightnode != None:
                aux1=buscamin(nodoaux.rightnode,comparo)
                if aux1>=comparo:
                  return aux1
            else:
                return comparo
                
def delete(bt,key):
    if bt.root != None: 
        deletenode=accessnodo(bt,key)
        if deletenode == None: #si el nodo no existe devuelve none
            return None
        else:
            deleting(bt,deletenode,key)
    elif bt.root.leftnode == None and bt.root.rightnode == None: #si solo queda la cabeza, borra sus datos y devuelve none
        bt.root.value=None
        bt.root.key=None
        return None
    else:
        return None #si no existe la cabeza devuelve none

def deleting(bt,deletenode,key):
    #CASO 1: El nodo a borrar es una hoja
    if deletenode.leftnode == None and deletenode.rightnode == None:
      borrador(deletenode,key)
      return
    #CASO 2: El nodo a borrar es una rama
    elif deletenode.leftnode != None:
        #pruebo primero por la izquierda
        aux=deletenode.leftnode.key
        nodoaux=deletenode.leftnode
        mayor=buscamax(nodoaux,aux) #busco el mayor de los menores
        deleteaux=accessnodo(bt, mayor) #accedo al nodo donde esta el mayor de los menores
       #--empiezo a borrar--#
        deletenode.value=deleteaux.value #cambio value por el mayor de menores
        deletenode.key=deleteaux.key#cambio key
        borrador(deleteaux,deleteaux.key) #borro el nodo mayor de menores
    elif deletenode.rightnode != None:
        aux=deletenode.rightnode.key
        nodoaux=deletenode.rightnode
        menor=buscamin(nodoaux,aux) #busco el mayor de los menores
        deleteaux=accessnodo(bt, menor) #accedo al nodo donde esta el mayor de los menores
       #--empiezo a borrar--#
        deletenode.value=deleteaux.value #cambio value por el mayor de menores
        deletenode.key=deleteaux.key#cambio key
        borrador(deleteaux,deleteaux.key) #borro el nodo mayor de menores

def borrador(deletenode,key):
  if deletenode.parent.leftnode.key==key:
      deletenode.parent.leftnode=None
      deletenode.parent=None
  else:
      deletenode.parent.rightnode=None
      deletenode.parent=None
 
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
insert(bt,1,1)
insert(bt,2,2)

amplitud(bt.root)
llave=input_int("Ingrese key del nodo a eliminar: ")
delete(bt,llave)
amplitud(bt.root)