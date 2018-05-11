class node:
  value=None
  nextnode=None
  
class linkedlist:
  head=None
  
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
    print("")
    currentnode2=currentnode2.nextnode
  print("")

def delete(linkedlist,element):
  currentnode=node()
  currentnode=linkedlist.head
  if linkedlist.head.value==element:
    linkedlist.head=currentnode.nextnode
  else:
    while currentnode != None:
      if currentnode.nextnode.value == element:
        currentnode.nextnode=currentnode.nextnode.nextnode
        break
      currentnode=currentnode.nextnode
      
def add(linkedlist,element):
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
    
def insert(linkedlist,element,pos):
  insertnode=node()
  insertnode.value=element
  currentnode=node()
  currentnode=linkedlist.head
  aux=0
  if pos == aux:
    insertnode.nextnode=linkedlist.head
    linkedlist.head=insertnode
  else:
    while pos-1 > aux:
      aux=aux+1
      currentnode=currentnode.nextnode
    insertnode.nextnode=currentnode.nextnode
    currentnode.nextnode=insertnode
  
def search(linkedlist,element):
  currentnode=node()
  currentnode=linkedlist.head
  aux=-1
  while currentnode != None:
    aux=aux+1
    if currentnode.value == element:
      return aux
    currentnode=currentnode.nextnode

def searchvalor(linkedlist,pos):
  currentnode=node()
  currentnode=linkedlist.head
  for a in range(0,pos):
    currentnode=currentnode.nextnode
  return currentnode.value
    
def imprimirmat(m,n):
	for i in range(0,n):
		print('[ ',end='')
		for j in range(0,n):
			print(m[i][j],'',end='')
		print(']')

def imprimirvector(m,n):
	for i in range(0,n):
		print('[',end='')
		print(m[i],end=']')
	print('')
		
def factorial(x):
  fact=1
  for a in range(x,0,-1):
    fact=fact*a
  return fact