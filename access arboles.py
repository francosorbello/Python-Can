#from colorama import init, Fore, Back, Style
from algo1 import *
from arboless import *

def preorden(bt):
  printnode=btreenode()
  printnode=bt.root
  printing(bt,printnode)
  print("")

def printing(bt,printnode):
  print(end='[')
  print(printnode.value,end=']')
  if printnode.leftnode != None:
    printing(bt,printnode.leftnode)
  if printnode.rightnode != None:
    printing(bt,printnode.rightnode)


def search(bt,element):
  recorre=bt.root
  aux=buscando(recorre,element)
  return aux
  
def buscando(recorre,element):
  print(recorre.value,element)
  if recorre.value==element:
    return recorre.value
  if recorre.leftnode != None:
    aux1=buscando(recorre.leftnode,element)
    if aux1 == element:
      return aux1
  if recorre.rightnode != None:
    aux1=buscando(recorre.rightnode,element)
    if aux1 == element:
      return aux1
  if recorre == None:
    return None
    
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

class btree:
  root=None

class btreenode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None

rootnobt=btreenode()
rootnobt.key=6
rootnobt.value=6
bt=btree()
bt.root=rootnobt

insert(bt,4,4)
insert(bt,3,3)
insert(bt,5,5)
insert(bt,8,8)
insert(bt,9,9)
insert(bt,7,7)

#n=input_int("Inserte cantidad de elementos:")

#for a in range(0,n):
#  key=input_int("Inserte key")
#  value=input_int("Inserte valor")
#  insert(bt,key,value)
preorden(bt)
element=input_int("Ingrese lo que busca:")
preorden(bt)
llavebusco=search(bt,element)
print("Key:",llavebusco)
