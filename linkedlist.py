#----COLAS Y PILAS----#

def enqueue(linkedlist,element):
#--Con esta función accedo a una cola--#
  newnode=node()
  newnode.value=element
  currentnode=node()
  currentnode=linkedlist.head
  if linkedlist.head == None:
    linkedlist.head=newnode
  else:
    while currentnode.nextNode !=None:
      currentnode=currentnode.nextNode
    currentnode.nextNode=newnode
    
def dequeue(linkedlist):
#--Con esta función saco el primer elemento en entrar--#
  deletenode=node()
  deletenode=linkedlist.head
  if deletenode !=None:
    auxnode=deletenode
    aux=deletenode.value
    linkedlist.head=deletenode.nextNode
    return auxnode
  else:
    print("None")
    return None
    
def push(linkedlist,element):
#--Con esta función agrego elementos a una pila--#
  newnode=node()
  newnode.value=element
  currentnode=node()
  currentnode=linkedlist.head
  if linkedlist.head == None:
    linkedlist.head=newnode
  else:
    while currentnode.nextNode !=None:
      currentnode=currentnode.nextNode
    currentnode.nextNode=newnode
    
def pop(linkedlist):
#--Con esta función saco el ultimo elemento en entrar--#
  deletenode=node()
  deletenode=linkedlist.head
  while deletenode.nextNode != None:
    if deletenode.nextNode.nextNode == None:
      print(deletenode.nextNode.value)
      aux=deletenode.nextNode.value
      deletenode.nextNode=None
      return aux
    deletenode=deletenode.nextNode
  print(deletenode.value)
  linkedlist.head=None
  print("None")
  return None
  
#----LISTAS----#

def add(linkedlist,element):
#--Con esta función agrego un elemento a la lista--#
  newnode=node()
  newnode.value=element
  newnode.nextNode=linkedlist.head
  linkedlist.head=newnode
  
def append(linkedlist,element):
#--Con esta función agrego un elemento a la lista--#
  newnode=node()
  newnode.value=element
  currentnode=node()
  currentnode=linkedlist.head
  if linkedlist.head == None:
    linkedlist.head=newnode
  else:
    while currentnode.nextNode !=None:
      currentnode=currentnode.nextNode
    currentnode.nextNode=newnode

def search(linkedlist,element):
#--Con esta función busco un nodo de la lista y devuelvo su posición--#
  currentnode=node()
  currentnode=linkedlist.head
  aux=-1
  while currentnode != None:
    aux=aux+1
    if currentnode.value == element:
      return aux
    currentnode=currentnode.nextNode
    
def insert(linkedlist,element,pos):
#--Con esta función inserto un nuevo nodo--#
  tamaño=length(linkedlist)
  insertnode=node()
  insertnode.value=element
  currentnode=node()
  currentnode=linkedlist.head
  aux=0
  if pos > tamaño:
      return None
  if pos == aux:
    insertnode.nextNode=linkedlist.head
    linkedlist.head=insertnode
    return pos
  elif pos==tamaño:
      append(linkedlist,element)
      return pos
  else:
    while pos-1 > aux:
      aux=aux+1
      currentnode=currentnode.nextNode
    insertnode.nextNode=currentnode.nextNode
    currentnode.nextNode=insertnode
    return pos
    
def delete(linkedlist,element):
#--Con esta función elimino un nodo--#
  currentnode=node()
  currentnode=linkedlist.head
  if currentnode != None:
    if linkedlist.head.value==element:
      linkedlist.head=currentnode.nextNode
    else:
      while currentnode != None:
        if currentnode.nextNode.value == element:
          currentnode.nextNode=currentnode.nextNode.nextNode
          break
        currentnode=currentnode.nextNode
  else:
    return None
      
def length(linkedlist):
#--Con esta función calculo la longitud de la lista(es decir, la cantidad de nodos)--#
  currentnode=node()
  currentnode=linkedlist.head
  aux=0
  while currentnode != None:
    aux=aux+1
    currentnode=currentnode.nextNode
  return aux
  
def update(linkedlist,element,position):
#--Con esta función cambio el valor de un nodo--#
  currentnode=node()
  currentnode=linkedlist.head
  tamaño=length(linkedlist)
  aux=0
  if tamaño<position:
    print("None")
    return None
  else:
    while aux<position:
      currentnode=currentnode.nextNode
      aux=aux+1
    currentnode.value=element
    return aux
    
def access(linkedlist,position):
#--Con esta función accedo al valor de un nodo--#
  currentnode=node()
  currentnode=linkedlist.head
  tamaño=length(linkedlist)
  if tamaño<position:
    return None
  else:
    aux=0
    while aux<position:
      currentnode=currentnode.nextNode
      aux=aux+1
    return currentnode.value

def imprimir(l):
#--Con esta función imprimo la lista--#
  currentnode2=node()
  currentnode2=l.head
  while currentnode2 != None:
    print('[',end='')
    print(currentnode2.value,end=']')
    currentnode2=currentnode2.nextNode
  print("")
    
class node:
  value=None
  nextNode=None
  
class LinkedList:
  head=None
  
L=LinkedList()