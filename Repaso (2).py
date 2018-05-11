from algo1 import *
from libreriafinal import *

class node:
    value=None
    nextNode=None
class LinkedList:
    head=None

l=LinkedList()

append(l,1)
append(l,2)
append(l,3)
append(l,4)
append(l,5)

l2=LinkedList()

append(l2,6)
append(l2,7)

currentder=l2.head
for b in range(medio+1,lengthLIST(l)):
    updateLIST(l,currentder.value,b)
    currentder=currentder.nextNode