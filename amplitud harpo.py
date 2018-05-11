from linkedlist import *

def amplitud(root):
	q=LinkedList()
	enqueue(q,root) # OJO estamos guardando un BTreeNode en el campo value de LinkedList
	while length(q) != 0: #mientras la lista no este vacia...
		node=dequeue(q) # recuperamos el value de LinkedList que es un BTreeNode y lo eliminamos de la lista
		print("[",node.value.key, ",",node.value.value,"]",end=',')
		if node.value.leftnode != None: # si hay algo por la izquierda, lo encolamos para imprimirlo despues
			enqueue(q,node.value.leftnode)
		if node.value.rightnode != None: # si hay algo por la derecha, hacemos lo mismo
			enqueue(q,node.value.rightnode)

def insertnode(rootnobt,insertonodo):
  if insertonodo.key<rootnobt.key:
    if rootnobt.leftnode==None:
      rootnobt.leftnode=insertonodo
      insertonodo.parent=rootnobt
    else:
      insertnode(rootnobt.leftnode,insertonodo)
  else:
    if rootnobt.rightnode==None:
      rootnobt.rightnode=insertonodo
      insertonodo.parent=rootnobt
    else:
      insertnode(rootnobt.rightnode,insertonodo)

def insert(bt,key,value):
  newnode=btreenode()
  newnode.key=key
  newnode.value=value
  if bt.root==None:
    bt.root=newnode
  else:
    insertnode(bt.root,newnode)

class node:
  value=None
  nextnode=None

class LinkedList:
  head=None

l=LinkedList()

class btree:
  root=None

class btreenode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None
  
rootnobt=btreenode()
#keycabeza=5
rootnobt.key=5
rootnobt.value=5
bt=btree()
bt.root=rootnobt

insert(bt,4,4)
insert(bt,3,3)
insert(bt,2,2)
insert(bt,6,6)
insert(bt,7,7)
insert(bt,8,8)
insert(bt,9,9)

amplitud(rootnobt)