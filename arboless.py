from linkedlist import *

def amplitud(root):
	q=LinkedList()
	enqueue(q,root) # OJO estamos guardando un BTreeNode en el campo value de LinkedList
	while length(q) != 0: #mientras la lista no este vacia...
		node=dequeue(q) # recuperamos el value de LinkedList que es un BTreeNode y lo eliminamos de la lista
		print("[ Key:",node.value.key, ", Value:",node.value.value,"]",end=',')
		if node.value.leftnode != None: # si hay algo por la izquierda, lo encolamos para imprimirlo despues
			enqueue(q,node.value.leftnode)
		if node.value.rightnode != None: # si hay algo por la derecha, hacemos lo mismo
			enqueue(q,node.value.rightnode)
	print("")
#--PREORDEN--#			
def preorden(bt):
  printnode=btreenode()
  printnode=bt.root
  printing(bt,printnode)
  print("")

def printing(bt,printnode):
  print(end='[')
  print(printnode.value,end=']')
  if printnode.leftnode != None:
    printing(bt,printnode.leftnode)
  if printnode.rightnode != None:
    printing(bt,printnode.rightnode)
    
#--ACCESS-#
def access(bt,llave):
    recorre=btreenode()
    recorre=bt.root
    nodoaux=accesing(recorre,llave)
    if nodoaux != None:
        return nodoaux.value
    else:
        return None
    
def accesing(recorre,llave):
    if recorre==None:
        return None
    elif recorre.key==llave:
        return recorre
    elif recorre.key>llave:
        return accesing(recorre.leftnode,llave)
    else:
        return accesing(recorre.rightnode,llave)
    
#--ACCESSNODO--#
def accessnodo(bt,llave):
    recorre=btreenode()
    recorre=bt.root
    nodoaux=accesingnodo(recorre,llave)
    if nodoaux != None:
        return nodoaux
    else:
        return None
    
def accesingnodo(recorre,llave):
    if recorre==None:
        return None
    elif recorre.key==llave:
        return recorre
    elif recorre.key>llave:
        return accesingnodo(recorre.leftnode,llave)
    else:
        return accesingnodo(recorre.rightnode,llave)

#--INSERT--#
def insertnode(rootnobt,insertonodo):
  if insertonodo.key<rootnobt.key:
    if rootnobt.leftnode==None:
      rootnobt.leftnode=insertonodo
      insertonodo.parent=rootnobt
    else:
      insertnode(rootnobt.leftnode,insertonodo)
  else:
    if rootnobt.rightnode==None:
      rootnobt.rightnode=insertonodo
      insertonodo.parent=rootnobt
    else:
      insertnode(rootnobt.rightnode,insertonodo)

def insert(bt,key,value):
  newnode=btreenode()
  newnode.key=key
  newnode.value=value
  if bt.root==None:
    bt.root=newnode
  else:
    insertnode(bt.root,newnode)

#--SEARCH--#
def search(bt,element):
  recorre=bt.root
  aux=buscando(recorre,element)
  return aux
  
def buscando(recorre,element):
  if recorre.value==element:
    return recorre.key
  if recorre.leftnode != None:
    aux1=buscando(recorre.leftnode,element)
    if aux1 != None: #CAMBIAR "AUX1 == ELEMENT"
      return aux1
  if recorre.rightnode != None:
    aux1=buscando(recorre.rightnode,element)
    if aux1 != None:
      return aux1
  if recorre == None:
    return None

#--DELETE--#
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

#--UPDATE--#
def update(bt,llave,element):
    nodoaux=accessnodo(bt,llave)
    if nodoaux != None:
        nodoaux.value=element
    else:
        return None

class node:
  value=None
  nextnode=None

class LinkedList:
  head=None

l=LinkedList()

class Btree:
  root=None

class btreenode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None