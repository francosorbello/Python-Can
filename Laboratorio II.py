from libreriafinal import *
from algo1 import *

def factorial(n):
    if n <= 1:
        return 1
    else:
        return(n*factorial(n-1))

def permutaciones(vectaux,l):
  a=1 #a comienza en 1 para saltarme el primer lugar
  b=0
  while b<factorial(len(vectaux)):#la cant de posibilidades es fact(n-1)
    aux=vectaux[a+1]#guardo el valor del siguiente para no perderlo
    vectaux[a+1]=vectaux[a]#muevo el valor a la derecha
    vectaux[a]=aux#muevo el valor del siguiente a la izquierda
    checkmovimiento(vectaux,l)
    print(vectaux)
    if a==len(vectaux)-2:#reinicio a para no pasarme de filas
        a=1
    else:
        a=a+1
    b=b+1

def agregoalista(array,L):
    auxarray=Array(len(array),0)
    for a in range(0,len(array)):
        auxarray[a]=array[a]
    appendLIST(L,auxarray)

def checkmovimiento(array,L):
    for x in range(0,8):
        comparo=array[x]
        for y in range(0,8):
            #checkeo en vertical
            if array[y]==comparo and y != x:
                aux= False #si esta var es distinta de falso luego guarda las posiciones
                return
            #checkeo en vertical hacia abajo
            if abs(comparo-x)==abs(array[y]-y) and y != x:  #dado que el diagonal de aij es a(i+x)(j+k), si los resto y da lo mismo entonces es diagonal
                aux= False #si esta var es distinta de falso luego guarda las posiciones
                return
            #checkeo en vertical hacia arriba
            if comparo+x==array[y]+y and y != x:  #dado que el diagonal de aij es a(i+x)(j+k), si los resto y da lo mismo entonces es diagonal
                aux= False #si esta var es distinta de falso luego guarda las posiciones
                return
    agegoalista(array,L)
    print("Movimiento correcto")
                
def permutacionesbruto(array,L):
    for r1 in range(0,8):
        for r2 in range(0,8):
            for r3 in range(0,8):
                for r4 in range(0,8):
                    for r5 in range(0,8):
                        for r6 in range(0,8):
                            for r7 in range(0,8):
                                for r8 in range(0,8):
                                    array[7]=r8
                                    checkmovimiento(array,L)
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

pos=Array(8,0)

aux=input_int("1. Por fuerza bruta | 2. Version mejorada: ")
if aux==1:
    permutacionesbruto(pos,L)
elif aux==2:
    for a in range(0,len(pos)):
        pos[a]=a+1
    permutaciones(pos,L)
