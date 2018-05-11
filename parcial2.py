from linkedlist import *

def buscaultimo(l):
    busca=node()
    busca=l.head
    while busca.nextNode!= None:
        busca=busca.nextNode  
    aux=busca.value
    return aux

def invertir(l):
    currentnode=l.head
    aux=0
    frozen=buscaultimo(l)
    print("debug frozen: ",frozen)
    while l.head.value != frozen:
        currentnode=l.head
        nodoaux=currentnode
        print("debug1: ",nodoaux.value)
        while currentnode.value != frozen:
            currentnode=currentnode.nextNode
        print("Debug2: ",currentnode.value)
        currentnode.nextNode=nodoaux
        currentnode=l.head
        l.head=currentnode.nextNode
        #delete(l,nodoaux.value)
        #aux=aux+1
        #currentnode=l.head
        #for a in range(0,aux):
            #currentnode=currentnode.nextNode

class node:
    value=None
    nextNode=None
    
class LinkedList:
    head=None
    
l=LinkedList()

x=int(input("ingrese cantidad de elementos: "))
for a in range(0,x):
      elem=int(input("Ingrese elemento: "))
      append(l,elem)

imprimir(l)
invertir(l)
print("Lista invertida:")

nodoprueba=l.head
for a in range(0,x):
    print(nodoprueba.value)
    nodoprueba=nodoprueba.nextNode
    