from libreriafinal import *
from algo1 import *
from time import time

ti=time()

def imprimir(l):
    currentnode=L.head
    while currentnode != None:
        print(currentnode.value)
        currentnode=currentnode.nextNode 

def listapermutaciones(L,array): #con esta funcion guardo las permutaciones en una lista
    arrayaux=Array(8,0)
    for b in range(0,8):
        arrayaux[b]=array[b]
    appendLIST(L,arrayaux)

def permutaciones(array,L): #esta funcion hace las permutaciones
    debug=0
    while debug<len(array)-1:
        a=0
        while a<len(array)-1:
            x=1
            while x<len(array)-1:
                #--PERMUTACION--#
                aux=array[x+1]#guardo el valor del siguiente para no perderlo
                array[x+1]=array[x]#muevo el valor a la derecha
                array[x]=aux#muevo el valor del siguiente a la izquierda
                x=x+1
                listapermutaciones(L,array) #esta funcion guarda las permutaciones en una lista
                print(array)
            a=a+1
        debug=debug+1
        cambioinicial(array,debug)
        if array[0]==len(array):
            debug=debug-1

def cambioinicial(array,a):
    aux=array[0]
    array[0]=array[a]
    array[a]=aux
    return
 
def permutaciones2(array,L):
    contador=0
    for r1 in range(0,8):
        for r2 in range(0,8):
            for r3 in range(0,8):
                for r4 in range(0,8):
                    for r5 in range(0,8):
                        for r6 in range(0,8):
                            for r7 in range(0,8):
                                for r8 in range(0,8):
                                    contador=contador+1
                                    array[7]=r8
                                    print(array)
                                array[6]=r7
                            array[5]=r6
                        array[4]=r5
                    array[3]=r4
                array[2]=r3
            array[1]=r2
        array[0]=r1
                               
class node:
  value=None
  nextnode=None
  
class linkedList:
  head=None
  
L=linkedList()

array=Array(8,0)

"""for a in range(0,8):
    array[a]=a+1"""

permutaciones2(array,L)
tf=time()
print("Tiempo:",tf-ti)
