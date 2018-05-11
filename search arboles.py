from arboless import *

def search(bt,element):
  recorre=bt.root
  aux=buscando(recorre,element)
  return aux
  
def buscando(recorre,element):
  if recorre.value==element:
    return recorre.key
  if recorre.leftnode != None:
    aux1=buscando(recorre.leftnode,element)
    if aux1 != None: #CAMBIAR "AUX1 == ELEMENT"
      return aux1
  if recorre.rightnode != None:
    aux1=buscando(recorre.rightnode,element)
    if aux1 != None:
      return aux1
  if recorre == None:
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

#n=input_int("Inserte cantidad de elementos:")

#for a in range(0,n):
#  key=input_int("Inserte key")
#  value=input_int("Inserte valor")
#  insert(bt,key,value)

element=int(input(("Ingrese lo que busca: ")))
preorden(bt)
llavebusco=search(bt,element)
print("Key:",llavebusco)