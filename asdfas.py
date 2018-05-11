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
    

class node:
  value=None
  nextNode=None

class LinkedList:
  head=None

L=LinkedList()

appendLIST(L,1)
appendLIST(L,2)
print(L.head.nextNode.value)
