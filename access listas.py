def access(linkedlist,position):
  currentnode=node()
  currentnode=linkedlist.head
  tamaño=length(linkedlist)
  if tamaño<position:
    return None
  else:
    aux=0
    while aux<position:
      currentnode=currentnode.nextnode
      aux=aux+1
    return currentnode

def length(linkedlist):
  currentnode=node()
  currentnode=l.head
  aux=0
  while currentnode != None:
    aux=aux+1
    currentnode=currentnode.nextnode
  return aux

def append(linkedlist,element):
  newnode=node()
  newnode.value=element
  currentnode=node()
  currentnode=linkedlist.head
  if linkedlist.head == None:
    linkedlist.head=newnode
  else:
    while currentnode.nextnode !=None:
      currentnode=currentnode.nextnode
    currentnode.nextnode=newnode
  
def imprimir(l):
  currentnode2=node()
  currentnode2=l.head
  while currentnode2 != None:
    print('[',end='')
    print(currentnode2.value,end=']')
    currentnode2=currentnode2.nextnode
  print("")
  
class node:
  value=None
  nextnode=None
  
class linkedlist:
  head=None
  
l=linkedlist

a=int(input(("Ingrese cantidad de elementos")))

for i in range (0,a):
  element=int(input(("Ingrese elemento:")))
  append(l,element)
imprimir(l)

asdf=int(input("Ingrese posicion elemento que busca:"))
nodoprueba=access(l,asdf)

print("Prueba",nodoprueba.value)

