from linkedlist import *

def burbuja(l):
    currentnode=node()
    currentnode=l.head
    large=length(l)-1#largo de la lista
    aux=0
    while large > aux:
        while currentnode.nextNode != None:
            if currentnode.value>currentnode.nextNode.value:
                aux2=currentnode.value#guardo el valor en una variable auxiliar
                currentnode.value=currentnode.nextNode.value
                currentnode.nextNode.value=aux2
                continue
            currentnode=currentnode.nextNode
        imprimir(l)
        print("--")
        aux=aux+1
        currentnode=l.head
    
        
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

"""append(L,4)
append(L,5)
append(L,1)
append(L,3)"""

a=int(input("Ingrese cant elementos:"))
for i in range (0,a):
    element=int(input(("Ingrese elemento:")))
    append(L,element)
imprimir(L)
burbuja(L)
print("Lista ordenada:")
imprimir(L)
