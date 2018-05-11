#from file1 import *
def access2(Btree , key ):
  if Btree.root == None :
    return None 
  else :
    k = subaccess(Btree.root , key )
    if k != None:
        return k.value
    
def subaccess (root , key ):
    if root == None:
        return None
    elif root.key == key:
        return root
    elif key < root.key:
        return subaccess(root.leftNode,key)
    else:
        return subaccess(root.rightNode,key)
    
def search(btree,value):
    if btree.root==None:
        return None
    else:
        return(searchNode(btree.root,value))
    
def searchNode(node,value):
    if node !=None:
        currentNode=node
        if value == currentNode.value:
            return(currentNode.key)
        else:
            rvalue=searchNode(currentNode.leftNode,value)
            if rvalue!=None:
                return(rvalue)
            rvalue=searchNode(currentNode.rightNode,value)
            if rvalue!=None:
                return(rvalue)

def access(bt,llave):
  recorre=bt.root
  if recorre.key==llave:
    return recorre
  elif llave<recorre.key:
    return accesing(bt,recorre.leftnode,llave)
  else:
    return accesing(bt,recorre.rightnode,llave)
    
def accesing(bt,recorre,element):
  if recorre.key==llave:
    return recorre
  else:
    if recorre.leftnode != None:
      return accesing(bt,recorre.leftnode,llave)
    if recorre.rightnode != None:
      return accesing(bt,recorre.rightnode,llave)

def delete(bt,key):
  deletenode=access2(bt,key)
  print("")
  print("debug:",deletenode.parent.value)
  if deletenode.leftnode == None and deletenode.rightnode == None:
    deletenode.parent=None
    return
  else:
    deleting(bt,key,deletenode)

def buscamax(deletenode):
  if deletenode != None:
    if deletenode.value >= aux:
      aux=deletenode.value
    buscamin(deletenode.rightnode)
  return aux

def buscamin(deletenode):
  if deletenode != None:
    if deletenode.value <= aux:
      aux=deletenode.value
    buscamin(deletenode.rightnode)
  return aux

def deleting(bt,key,deletenode):
    if deletenode.leftnode != None and deletenode.rightnode != None:
        aux=deletenode.rightnode.value
        menor=buscamin(deletenode.rightnode,aux)
        print("debug",menor)
        deletenodeaux=access(bt,menor) #en esta variable auxiliar guardo el nodo que reemplaza al que borro
        deletenode.value=deletenodeaux.value #reemplazo los valores
        deletenode.key=deletenodeaux.key #reemplazo la key
        deletenodeaux.parent=None
    else:
        if deletenode.leftnode != None:
            maxim=buscamax(deletenode.leftnode)
            
            
def deleting(bt)
             
def preorden(bt):
  printnode=btreenode()
  printnode=bt.root
  printing(bt,printnode)

def printing(bt,printnode):
  print(end='[')
  print(printnode.value,end=']')
  if printnode.leftnode != None:
    printing(bt,printnode.leftnode)
  if printnode.rightnode != None:
    printing(bt,printnode.rightnode)

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
rootnobt.key=5
rootnobt.value=5
bt=btree()
bt.root=rootnobt


insert(bt,3,3)
insert(bt,4,4)
insert(bt,2,2)
insert(bt,6,6)
insert(bt,7,7)
insert(bt,8,8)

#n=input_int("Inserte cantidad de elementos:")

#for a in range(0,n):
  #key=input_int("Inserte key")
  #value=input_int("Inserte valor")
  #insert(bt,key,value)

llave=int(input(("Ingrese la key del nodo a eliminar:")))
preorden(bt)
delete(bt,llave)
preorden(bt)