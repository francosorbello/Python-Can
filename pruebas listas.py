from libreriafinal import *
from algo1 import *

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

def invierto(l):
    largo=lengthLIST(l)
    lswap=LinkedList() #guardo la lista invertida en una nueva lista
    node=l.head
    for a in range(0,largo):
        aux=pop(l)
        appendLIST(lswap,aux)
    return lswap
    

class node:
    value=None
    nextNode=None
class LinkedList:
    head=None
    
l=LinkedList()
"""appendLIST(l,1)
appendLIST(l,2)
appendLIST(l,3)
appendLIST(l,4)
appendLIST(l,5)
imprimirLIST(l)
prueba=invierto(l)
print("Lista reordenada:")
imprimirLIST(prueba)"""
