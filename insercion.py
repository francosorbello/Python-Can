from linkedlist import *

def orden(l,valor):
    ordennode=node()
    ordennode=l.head
    pos=0
    while ordennode != None:
        if ordennode.value>valor:
            insert(l,valor,pos)
            break
        pos=pos+1
        ordennode=ordennode.nextNode
        
def insercion(L):
    currentnode=node()
    currentnode=L.head
    while currentnode.nextNode != None:
        if currentnode.value>currentnode.nextNode.value:
            aux=currentnode.nextNode.value
            delete(L,aux)
            orden(L,aux)
            continue
        currentnode=currentnode.nextNode
        imprimir(L)
        print("--")
            
        
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

append(L,4)
append(L,5)
append(L,1)
append(L,3)

#a=int(input("Ingrese cant elementos:"))
#for i in range (0,a):
    #element=int(input(("Ingrese elemento:")))
    #append(L,element)
imprimir(L)
insercion(L)
print("Lista ordenada:")
imprimir(L)