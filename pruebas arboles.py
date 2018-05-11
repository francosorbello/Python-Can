from arboless import *

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
        deleteaux=accessnodo(bt, menor) #accedo al nodo donde esta el mayor de los menore
        deletenode.value=deleteaux.value
        deletenode.key=deleteaux.key#cambio key
        borrador(deleteaux,deleteaux.key) #borro el nodo mayor de menores

def borrador(deletenode,key):
  if deletenode.parent.leftnode != None and deletenode.parent.leftnode.key==key:
      deletenode.parent.leftnode=None
      deletenode.parent=None
  else:
      deletenode.parent.rightnode=None
      deletenode.parent=None

class Btree:
  root=None

class btreenode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None

strings=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
keys=[10,5,20,8,13,22]
bt=Btree()
for a in range(0,6):
    insert(bt,keys[a],strings[a])
    
amplitud(bt.root)
delete(bt,5)
print("Nodo borrado")
amplitud(bt.root)
