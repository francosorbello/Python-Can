from algo1 import *
#--------------------ARBOLES--------------------#

#--AMPLITUD--#
def amplitudarbol(root):
	q=LinkedList()
	enqueuelist(q,root) # OJO estamos guardando un BTreeNode en el campo value de LinkedList
	while lengthLIST(q) != 0: #mientras la lista no este vacia...
		node=dequeueLIST(q) # recuperamos el value de LinkedList que es un BTreeNode y lo eliminamos de la lista
		print("[ Key:",node.value.key, ", Value:",node.value.value,"]",end=',')
		if node.value.leftnode != None: # si hay algo por la izquierda, lo encolamos para imprimirlo despues
			enqueueLIST(q,node.value.leftnode)
		if node.value.rightnode != None: # si hay algo por la derecha, hacemos lo mismo
			enqueueLIST(q,node.value.rightnode)
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
def accessarbol(bt,llave):
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

def insertarbol(bt,key,value):
  newnode=btreenode()
  newnode.key=key
  newnode.value=value
  if bt.root==None:
    bt.root=newnode
  else:
    insertnode(bt.root,newnode)

#--SEARCH--#
def searcharbol(bt,element):
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
                
def deletearbol(bt,key):
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
def updatearbol(bt,llave,element):
    nodoaux=accessnodo(bt,llave)
    if nodoaux != None:
        nodoaux.value=element
    else:
        return None
        
#--------------------ARRAYS--------------------#

#--SEARCH--#
def searchARR(array,element):
  aux=None
  for i in range(0,len(array)):
    if array[i]==element:
      aux=i
      break
  return aux

#--INSERT--# 
def insertARR(array,element,index):
  count=lengthARR(array)
  if count !=0:
    aux=len(array)
    if index>aux:
      return None
    else:
      if array[index]==None:
          array[index]=element
      else:
          for a in range(len(array)-1,index,-1):
            array[a]=array[a-1]
          array[index]=element
  else:
    return None
  
#--DELETE--#
def deleteARR(array,element):
  pos=search(array,element)
  if pos == None:
      return pos
  else:
      array[pos]=None
      for j in range(pos,len(array)-1):
        array[j]=array[j+1]
        array[j+1]=None

#--LENGTH--#
def lengthARR(array):
    aux=len(array)
    count=0
    for a in range(0,aux):
        if array[a] != None:
            count=count+1
    return count

#--ENQUEUE--#    
def enqueueARR(array,element):
    index=len(array)-1 #ultima pos del vector
    aux=0 #si el vector esta lleno entra en la primera posicion
    for a in range(0,index):
        if array[a]==None: #busco espacios vacios para insertar
            aux=a
            break
    insertARR(array,element,aux)

#--DEQUEUE--#
def dequeueARR(array):
    count=length(array)
    if count>0:
        aux=array[0]
        deleteARR(array,aux)
        return aux
    else:
        return None
#--PUSH--#        
def pushARR(array,element):
    count=length(array)
    if count !=0:
        index=len(array)-1 #ultima pos del vector
        aux=index #si el vector no está vacio inserta en la ultima pos
        for a in range(0,index):
            if array[a]==None: #busco espacios vacios para insertar
                aux=a
                break
        insertARR(array,element,aux)
    else:
        array[0]=element

#--POP--#  
def popARR(array):
    count=length(array)
    if count != 0:
        index=len(array)-1
        for a in range(index,1,-1):
            if array[a] != None:
                aux=a #guardo primera pos distina de 0
                break
        borro=array[aux]
        deleteARR(array,borro)
        return borro
    else:
        return None
#--Print para matrices--#
def imprimirMAT(matriz,m,n):
    for i in range(0,m):
        for j in range(0,n):
            #print('[',end='')
            print("[",matriz[i][j],end=']')
        print("")

#--------------------LISTAS--------------------#

#----COLAS Y PILAS----#

def enqueue(linkedlist,element):
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
  deletenode=node()
  deletenode=linkedlist.head
  if deletenode !=None:
    aux=deletenode.value
    linkedlist.head=deletenode.nextNode
    return aux
  else:
    print("None")
    return None
    
def push(linkedlist,element):
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
  deletenode=node()
  deletenode=linkedlist.head
  """if l.head.nextNode==None:
      aux=l.head.value
      l.head=None
      return aux"""
  while deletenode.nextNode != None:
    if deletenode.nextNode.nextNode == None:
      aux=deletenode.nextNode.value
      deletenode.nextNode=None
      return aux
    deletenode=deletenode.nextNode
  aux=linkedlist.head.value
  linkedlist.head=None
  return aux
  
#----LISTAS----#

def addLIST(linkedlist,element):
  newnode=node()
  newnode.value=element
  newnode.nextNode=linkedlist.head
  linkedlist.head=newnode
  
def appendLIST(linkedlist,element):
  newnode=node()
  newnode.value=element
  currentnode=node()
  currentnode=linkedlist.head
  if linkedlist.head == None:
    linkedlist.head=newnode
  else:
    while currentnode.nextNode != None:
      currentnode=currentnode.nextNode
    currentnode.nextNode=newnode

def searchLIST(linkedlist,element):
  currentnode=node()
  currentnode=linkedlist.head
  aux=-1
  while currentnode != None:
    aux=aux+1
    if currentnode.value == element:
      return aux
    currentnode=currentnode.nextNode
    
def insertLIST(linkedlist,element,pos):
  tamaño=lengthLIST(linkedlist)
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
      appendLIST(linkedlist,element)
      return pos
  else:
    while pos-1 > aux:
      aux=aux+1
      currentnode=currentnode.nextNode
    insertnode.nextNode=currentnode.nextNode
    currentnode.nextNode=insertnode
    return pos
    
def deleteLIST(linkedlist,element):
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
      
def lengthLIST(linkedlist):
  currentnode=node()
  currentnode=linkedlist.head
  aux=0
  while currentnode != None:
    aux=aux+1
    currentnode=currentnode.nextNode
  return aux
  
def updateLIST(linkedlist,element,position):
  currentnode=node()
  currentnode=linkedlist.head
  tamaño=lengthLIST(linkedlist)
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
    
def accessLIST(linkedlist,position):
  currentnode=node()
  currentnode=linkedlist.head
  tamaño=lengthLIST(linkedlist)
  if tamaño<position:
    return None
  else:
    aux=0
    while aux<position:
      currentnode=currentnode.nextNode
      aux=aux+1
    return currentnode.value

def accessnodoLIST(linkedlist,position):
  currentnode=node()
  currentnode=linkedlist.head
  tamaño=lengthLIST(linkedlist)
  if tamaño<position:
    return None
  else:
    aux=0
    while aux<position:
      currentnode=currentnode.nextNode
      aux=aux+1
    return currentnode
    
def imprimirLIST(l):
  currentnode2=node()
  currentnode2=l.head
  while currentnode2 != None:
    print('[',end='')
    print(currentnode2.value,end=']')
    currentnode2=currentnode2.nextNode
  print("")

def swapLIST(L,i,j):
    current=L.head
    current2=L.head
    for a in range(0,i):
        current=current.nextNode
    aux=current.value
    for a in range(0,j):
        current2=current2.nextNode
    current.value=current2.value
    current2.value=aux
    
class node:
  value=None
  nextNode=None

class LinkedList:
  head=None

L=LinkedList()

class Btree:
  root=None

class btreenode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None