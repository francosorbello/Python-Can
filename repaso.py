from algo1 import *
from libreriafinal import *

def abs(x):
    if x<0:
        return (-x)
    else
        return x
    
def reordeno(lizq,lder,l):
    medio=lengthLIST(l)//2
    currentizq=lizq.head
    for a in range(0,medio):
        updateLIST(l,currentizq.value,a)
        currentizq=currentizq.nextNode
    currentder=lder.head
    for b in range(medio,lengthLIST(l)):
        updateLIST(l,currentder.value,b)
        currentder=currentder.nextNode
    return l
    

def separo(lizq,lder,l):
    medio=lengthLIST(l)//2
    currentnode=l.head
    aux=0
    #Separo pares e impares en 2 listas 
    while currentnode.nextNode !=None:
        if (abs(currentnode.value)-(abs(currentnode.value)%1))%2==0 and aux!=medio:
            appendLIST(lder,currentnode.value)
        elif aux!=medio:
            appendLIST(lizq,currentnode.value)
        aux=aux+1
        currentnode=currentnode.nextNode
    selectionSort(lder)#ordeno pares descendentes
    selectionSort(lizq)#ordeno impares ascendentes


class node:
    value=None
    nextNode=None
class LinkedList:
    head=None

l=LinkedList()
#appendLIST(l,-218.34)
#appendLIST(l,-29.48)
#appendLIST(l,45.8)
#appendLIST(l,66.95)
#appendLIST(l,86.18)

append(l,1)
append(l,2)
append(l,3)
append(l,4)
append(l,5)

currentnode=node()
currentnode=l.head

medio=lengthLIST(l)//2
print(medio)

while currentnode.nextNode != None:
    currentnode=currentnode.nextNode

swapLIST(l,medio,4) #pongo el mayor en el medio
lizq=LinkedList()
lder=LinkedList()
separo(lizq,lder,l)
junto(lizq,lder,l)