from arboless import amplitud , insert

# Devolver el nodo que contiene la key y None en caso contrario.
def getNode(btree,key):
# buscar el nodo que contiene la key
    if btree.root==None:
        return None
    else:
        node=accessNode(btree.root,key)
        if node != None:
            return(node)
        else:
            return None

def delete(btree,key):
	print("a borrar la key:",key)
	noded=getNode(btree,key)
	if noded!=None:
		print("se encuentra con el valor",noded.value)
		#tiene hijos izq?
		if noded.leftnode!=None:
			#tiene derecho?
			if noded.rightnode!=None:
				print("tiene ambos hijos")
				
				if noded.rightnode.leftnode!=None:
					print("tomo el menor de sus mayores")
					#soy hijo izquierdo o derecho?
					if noded.parent.leftnode!=None:
						if noded.parent.leftnode.key==key:
							print("soy hijo izquierdo")
							noded.parent.leftnode=noded.rightnode.leftnode
						else:
							print("soy hijo derecho")
							noded.parent.rightnode=noded.rightnode.leftnode
						delete(btree,noded.rightnode.leftnode.key)
				elif noded.leftnode.rightnode!=None:
					print("tomo el mayor del menor")
					#soy hijo izquierdo o derecho?
					if noded.parent.leftnode!=None:
						if noded.parent.leftnode.key==key:
							print("soy hijo izquierdo")
							noded.parent.leftnode=noded.leftnode.rightnode
						else:
							print("soy hijo derecho")
							noded.parent.rightnode=noded.leftnode.rightnode
						delete(btree,noded.rightnode.leftnode.key)
			else:
				print("tiene solo hijo izquierdo")
				if noded.parent.leftnode!=None:
					if noded.parent.leftnode.key==noded.key:
						print("soy hijo izquierdo")
						noded.parent.leftnode=noded.leftnode
					else:
						print("soy hijo derecho")
						noded.parent.rightnode=noded.leftnode
				else:
						print("soy hijo derecho")
						noded.parent.rightnode=noded.leftnode
		else:
			if noded.rightnode!=None:
				print("tiene solo hijo derecho")
				if noded.parent.leftnode!=None:
					if noded.parent.leftnode.key==noded.key:
						print("soy hijo izquierdo")
						noded.parent.leftnode=noded.rightnode
					else:
						print("soy hijo derecho")
						noded.parent.rightnode=noded.rightnode
				else:
						print("soy hijo derecho")
						noded.parent.rightnode=noded.rightnode
			else:
				print("no tiene hijos")
				if btree.root.key==noded.key:
					print("es el root")
					btree.root=None
				else:
					if noded.parent.rightnode!=None:
						if noded.parent.rightnode.key==noded.key:
							noded.parent.rightnode=None
							print("eliminada rama derecha del padre")
					if noded.parent.leftnode!=None:
						if noded.parent.leftnode.key==noded.key:
							noded.parent.leftnode=None
							print("eliminada rama izquierda del padre")
	else:
		print("no se encuentra:",key)
		return None

    
# buscar el nodo que contiene la key
def accessNode(root,key):
    currentNode=root
    
    if not currentNode:
        return None
    elif currentNode.key == key:
        return currentNode
    elif key < currentNode.key:
        return accessNode(currentNode.leftnode,key)
    else:
        return accessNode(currentNode.rightnode,key)

# Devolver el valor del nodo que contiene la key y None en caso contrario.
def access(btree,key):
    if btree.root==None:
        return None
    else:
        node=accessNode(btree.root,key)
        if node != None:
            return(node.value)
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
insert(bt,1,1)

amplitud(bt.root)
llave=int(input(("Ingrese key del nodo a eliminar: ")))
delete(bt,llave)
amplitud(bt.root)
