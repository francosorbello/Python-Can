# Implementacion de un binary heap
# Algoritmos y estructuras de datos I
# Ingenieria - Uncuyo
# harpomaxx@gmail.com
# jue oct 26 09:24:47 ART 2017

# Ejercitacion: Implementar las operaciones y las porciones de codigo faltantes

from libreriafinal import *
#from random import randint

class Bheap:
    """ Estructura Bheap, lo unico que tiene una referencia a un lista."""
    bheaplist=LinkedList()
    def __str__(self):
            """ Permite hacer un print a una estructura Bheap"""
            str_list=""
            current=self.bheaplist.head.nextNode
            while current!=None:
                str_list= str_list+str(current.value)+" "
                current=current.nextNode
            return(str_list)


def delMax(BH):
    """ Recupera el mayor elemento del heap. Este siempre se encontrara al comienzo (posicion 1).
        Para manter la esctrucura del arbol binario se reemplaza el nodo raiz por el ultimo nodo.
        
        Luego mediante la funcion shiftDown se va recorriendo el arbol hasta encontrar la posicion 
        correcta de dicho nodo. De esta manara se garantiza la propiedad heap.
    """
    i=lengthLIST(BH.bheaplist)-1 #obtengo la ultma posicion
    if i >1:
        valorcambio=accessLIST(BH.bheaplist,i) #guardo el valor del ultimo nodo
        retval=BH.bheaplist.head.nextNode.value #devuelvo el valor de la raiz del arbol
        deleteLIST(BH.bheaplist,valorcambio) #elimino el nodo que pasa a ser la raiz
        BH.bheaplist.head.nextNode.value=valorcambio
        i=1
        shiftDown(BH,i)
        return retval
    elif i==1:
        retval=BH.bheaplist.head.nextNode.value
        BH.bheaplist.head.nextNode.value=None
        return retval
    else:
        return None


def shiftUp(BH,i):
    """ Recorre el arbol desde los nodos hacia la raiz y va reemplazando el nodo i por su padre
        siempre y cuando i sea mayor. La operacion matematica i // 2 nos permite rapidamente encontrar al padre.
    """
    while i//2>0:
        imprimirLIST(BH.bheaplist)
        nodopadre=accessnodoLIST(BH.bheaplist,i//2) #accedo al nodo padre
        current=accessnodoLIST(BH.bheaplist,i)#accedo al nodo que ingreso
        if current.value<nodopadre.value:
            aux=nodopadre.value
            nodopadre.value=current.value
            current.value=aux
        i = i // 2 #condicion de salida
    print("Lista ordenada:")
    imprimirLIST(BH.bheaplist)
    print("---")

def shiftDown(BH,i,currentsize=None):
    """ Recorre el arbol desde la raiz y hacia los nodos (arriba hacia abajo) va reemplazando el nodo i por sus hijos siempre y cuando alguno de sus hijos sea mayor."""
    if currentsize==None:
        currentsize=lengthLIST(BH.bheaplist)-1
    while (i * 2) <= currentsize:
        mc = maxChild(BH,i,currentsize) #Determina dado un nodo i, cual de sus hijos es el mayor y devuelve la posicion
        #print("mc:",mc,"| i:",i)
        if accessLIST(BH.bheaplist,mc) < accessLIST(BH.bheaplist,i):
            hijomenor=accessnodoLIST(BH.bheaplist,mc-1) #accedo al hijo menor
            nodopadre=accessnodoLIST(BH.bheaplist,i) #accedo al padre
            aux=hijomenor.value
            #--intercambio valores--#
            hijomenor.value=nodopadre.value
            nodopadre.value=aux
        i = mc

def maxChild(BH,i,currentsize): #¿POR QUE MAXCHILD ME DEVUELVE EL MAYOR SI YO NECESITO EL MENOR PARA CAMBIAR?
    """ Determina dado un nodo i, cual de sus hijos es el mayor y devuelve la posicion 
    """
    if i * 2 + 1 > currentsize: #me aseguro de no salirme de la lista
        return i * 2
    else:
        if accessLIST(BH.bheaplist,i*2) > accessLIST(BH.bheaplist,i*2+1):
            return i * 2 
        else:
            return i * 2 + 1
    
def insert(BH,k):
    """ Inserta un elemento en el heap. Si la lista esta vacia, se crea un elemento 0. Este ultimo no se utiliza,
        pero facilita las operaciones matematicas para acceder a los padres e hijos. 
    """
    pos=lengthLIST(BH.bheaplist)
    if pos==0:
        addLIST(BH.bheaplist,0)
        pos=pos+1
    insertLIST(BH.bheaplist,k,pos)
    currentsize=lengthLIST(BH.bheaplist)-1
    shiftUp(BH,currentsize)

def heapify(BH,L):
    """ Dada una lista crea un heap con complejidad temporal O(n)
    """
    i = lengthLIST(L) // 2
    BH.bheaplist.head = L.head #"agrega" la lista a BH  para despues trabajar con ella
    addLIST(BH.bheaplist,0)
    while (i > 0):
        shiftDown(BH,i)
        i = i - 1

def length(BH):
    return lengthLIST(BH.bheaplist)-1

"""if __name__ == "__main__":
    H=Bheap()
    insert(H,8)
    insert(H,1)
    insert(H,5)
    insert(H,4)
    print(H)
    minimun=delMax(H)
    print(H)
    print("----")
    L=linkedlist.LinkedList()
    addLIST(L,4)
    addLIST(L,3)
    addLIST(L,2)
    addLIST(L,1)
    addLIST(L,12)
    addLIST(L,255)
    addLIST(L,1000)
    print(L)
    heapify(H,L)
    print(H)"""

class node:
  value=None
  nextnode=None

class LinkedList:
  head=None

L=LinkedList()
H=Bheap()
insert(H,8)
insert(H,1)
insert(H,5)
insert(H,4)
print(H)
minimun=delMax(H)
print(H,"elemento borrado:",minimun)
print("----")
L=LinkedList()
addLIST(L,4)
addLIST(L,3)
addLIST(L,2)
addLIST(L,1)
addLIST(L,12)
addLIST(L,255)
addLIST(L,1000)
print("Lista a heapyfiar:")
imprimirLIST(L)
heapify(H,L)
print("After heapify")
print(H)