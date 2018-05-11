from file1 import *

def append(linkedlist,unempleado):
  newnode=node()
  newnode.value=unempleado
  currentnode=node()
  currentnode=linkedlist.head
  if linkedlist.head == None:
    linkedlist.head=newnode
  else:
    while currentnode.nextnode !=None:
      currentnode=currentnode.nextnode
    currentnode.nextnode=newnode

def add(linkedlist,unempleado):
  newnode=node()
  newnode.value=unempleado
  newnode.nextnode=linkedlist.head
  linkedlist.head=newnode
  
def imprimir(l):
  currentnode2=node()
  currentnode2=l.head
  while currentnode2 != None:
    print('[',end='')
    print(currentnode2.value.nombre , currentnode2.value.edad , currentnode2.value.nrolegajo , end=']')
    print("")
    currentnode2=currentnode2.nextnode
  print("")

class empleado:
  nombre=None
  edad=None
  nrolegajo=None

class node:
  value = None
  nextnode=None
  
class linkedlist:
  head=None
  
l=linkedlist()

unempleado=empleado()

a=int(input("Ingrese cantidad de empleados:")

for s in range(0,a) 
  unempleado.nombre=input("Ingrese el nombre del empleado:")
  unempleado.edad=int(input("Ingrese edad:")
  unempleado.nrolegajo=int(input("Ingrese legajo:")
  append(l,unempleado)
  print("")
  print("Cargado.Los datos son:")
  imprimir(l)

#imprimir(l)

pruebaleer=node()
pruebaleer=l.head
print(pruebaleer.value.edad)
print(pruebaleer.nextnode.value.edad)