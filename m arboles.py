#from file1 import *
from milib import *

def amplitud(bt,l):
  printnode=btreenode()
  printnode=bt.root
  append(l,printnode.value)
  printing(bt,printnode,l)
  #printing2(l,printnode)

def printing2(l,printnode):
  append(l,printnode.value)
  if printnode.leftnode != None:
    printing2(l,printnode.leftnode)
  if printnode.rightnode != None:
    printing2(l,printnode.rightnode)
  
def printing(bt,printnode,l):
  if printnode.leftnode != None and printnode.rightnode != None:
    #append(l,printnode.leftnode.value)
    #append(l,printnode.rightnode.value)
    print(printnode.leftnode.value)
    print(printnode.rightnode.value)
    printing(bt,printnode.leftnode,l)
    printing(bt,printnode.rightnode,l)
  else:
    if printnode.leftnode != None:
        print(printnode.leftnode.value)
       # append(l,printnode.leftnode.value)
        printing(bt,printnode.leftnode,l)
    elif printnode.rightnode != None:
        print(printnode.rightnode.value)
        #append(l,printnode.rightnode.value)
        printing(bt,printnode.rightnode,l) 
    
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

class linkedlist:
  head=None

l=linkedlist()

class btree:
  root=None

class btreenode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None

rootnobt=btreenode()
#keycabeza=input_int("Ingrese key de la cabeza")
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
#n=input_int("Inserte cantidad de elementos:")

#for a in range(0,n):
#  key=input_int("Inserte key")
#  value=input_int("Inserte valor")
#  insert(bt,key,value)

amplitud(bt,l)
#imprimir(l)