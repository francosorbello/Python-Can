from algo1 import *
from arboless import *

def update(bt,llave,element):
    nodoaux=accessnodo(bt,llave)
    if nodoaux != None:
        nodoaux.value=element
    else:
        return None

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

amplitud(bt.root)
element=input_int("Ingrese valor a introducir: ")
llave=input_int("Ingrese key del nodo donde va a cambiar el valor: ")
update(bt,llave,element)
preorden(bt)