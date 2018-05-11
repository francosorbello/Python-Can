from linkedlist import *

def acceder(l,aux):#esta funcion accede a un nodo dada una posicion
    accessnode=l.head
    for a in range(0,aux):
        accessnode=accessnode.nextNode
    return accessnode

def buscamenor(l):
    busca=l.head #busca y devuelve el nodo con el value mas chico
    menor=busca.value
    while busca !=None:
        if busca.value<menor:
            return busca

def seleccion(l):
    currentnode=node()
    currentnode=l.head
    aux=0 #con este auxiliar guardo 
    while currentnode.nextNode != None:
        menor=currentnode.value
        while currentnode !=None: 
            if currentnode.value<menor: #obtengo el valor mas chico
                menor=currentnode.value
            currentnode=currentnode.nextNode
    #--hago el cambio--#
        pos=search(l,menor) #obtengo la posicion del nodo donde esta el menor
        nodomenor=acceder(l,pos)#accedo al nodo con el menor value
        currentnode=acceder(l,aux)#accedo al nodo donde voy a cambiar
        auxcambio=currentnode.value #guardo un value en una variable auxiliar
        currentnode.value=nodomenor.value
        nodomenor.value=auxcambio
        aux=aux+1
        currentnode=currentnode.nextNode
        
class node:
  value=None
  nextNode=None
  
class LinkedList:
  head=None
  
L=LinkedList()


#add(L,4)
#add(L,5)
#add(L,1)
#add(L,3)

#append(L,4)
#append(L,5)
#append(L,1)
#append(L,3)

a=int(input("Ingrese cant elementos:"))
for i in range (0,a):
    element=int(input(("Ingrese elemento:")))
    append(L,element)
imprimir(L)
seleccion(L)
print("Lista ordenada:")
imprimir(L)