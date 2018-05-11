from algo1 import *
from libreriafinal import *

def swap(L,i,j):
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
appendLIST(L,12)
appendLIST(L,1)
appendLIST(L,5)
appendLIST(L,16)
imprimirLIST(L)

swap(L,0,3)
imprimirLIST(L)