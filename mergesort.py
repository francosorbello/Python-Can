from libreriafinal import *
from algo1 import *

def subList(L,startpos,endpos):
    newL=LinkedList()
    cn=L.head
    for i in range(0,startpos):
        cn=cn.nextNode
    addLIST(newL,cn.value)     
    for i in range(startpos+1,endpos):
       cn=cn.nextNode
       insertLIST(newL,cn.value,lengthLIST(newL))
    return newL

def junto(l,laux):
    ljunto=LinkedList()
    while l.head != None and laux.head!=None:
      if l.head.value<=laux.head.value:
          aux=dequeue(l)
          appendLIST(ljunto,aux)
      else:
          aux=dequeue(laux)
          appendLIST(ljunto,aux)
    while l.head != None:
          aux=dequeue(l)
          appendLIST(ljunto,aux)
    while laux.head != None:
          aux=dequeue(laux)
          appendLIST(ljunto,aux)
    return ljunto
 
def mergesort(l):
    print("Antes:")
    imprimirLIST(l)
    if lengthLIST(l)>1:
        largo=lengthLIST(l)
        lizq=subList(l,0,largo//2)
        lder=subList(l,largo//2,largo)
        mergesort(lizq)
        mergesort(lder)
        return junto(lizq,lder)
    print("despues:")
    imprimirLIST(l)
    
class node:
    value=None
    nextNode=None

class LinkedList:
    head=None

L=LinkedList()

appendLIST(L,38)
appendLIST(L,27)
appendLIST(L,43)
appendLIST(L,3)
appendLIST(L,9)
appendLIST(L,82)
appendLIST(L,10)
appendLIST(L,12)

aux=mergesort(L)
print("Se ordena?")
imprimirLIST(aux)