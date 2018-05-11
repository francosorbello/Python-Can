from algo1 import *
from milib import *
import random

def buscomejor(lr):
  currentnode2=node()
  currentnode2=lr.head
  menor=currentnode2.value
  while currentnode2 != None:
    if currentnode2.value <= menor:
      menor=currentnode2.value
    currentnode2=currentnode2.nextnode
  return menor

def calculacostos(m,l,lr,n):
  currentnode=node()
  currentnode=l.head
  while currentnode !=None:
    costo=0
    for aux in range(0,n-1):
      i=currentnode.value[aux]
      j=currentnode.value[aux+1]
      costo=costo+m[i][j]
    append(lr,costo)
    currentnode=currentnode.nextnode
  print("Valor de los caminos:")
  imprimir(lr)

def buscarutas(vectaux,l,j):
  a=1 #a comienza en 1 para saltarme el primer lugar
  b=0
  while b<factorial(len(vectaux)-1):#la cant de posibilidades es fact(n-1)
    aux=vectaux[a+1]#guardo el valor del siguiente para no perderlo
    vectaux[a+1]=vectaux[a]#muevo el valor a la derecha
    vectaux[a]=aux#muevo el valor del siguiente a la izquierda
    imprimirvector(vectaux,len(vectaux))
    vectorauxiliar=Array(len(vectaux),0)#en este vectorauxiliar guardo el recorrido
    for z in range(0,len(vectaux)):
      vectorauxiliar[z]=vectaux[z]#este bucle pasa el recorrido a vectorauxiliar
    append(l,vectorauxiliar)#aca lo agrego a una lista para un acceso mas facil
    if a==len(vectaux)-2:#reinicio a para no pasarme de filas
      a=1
    else:
      a=a+1
    b=b+1
  
n=input_int("Ingrese la cantidad de ciudades:")
m=Array(n,Array(n,0))
vectaux=Array(n,0)#de este vector obtengo los caminos posibles

for i in range(0,n):
  vectaux[i]=i #cada i representa una ciudad. EJ: 0 es la ciudad A,1 la B,etc.
  for j in range(i+1,n):
    m[i][j]=random.randrange(1,100)
    m[j][i]=m[i][j]
imprimirmat(m,n)
imprimirvector(vectaux,n)

class ruta:
  fila=None
  col=None
  
class linkedlist:
  head=None
  
class node:
  value=None
  nextnode=None

lr=linkedlist()
l=linkedlist()

j=0
aux=0

buscarutas(vectaux,l,j)

calculacostos(m,l,lr,n)

minim=buscomejor(lr)
pos=search(lr,minim)
camino=searchvalor(l,pos)

print("El camino mas corto es:",minim,".El recorrido es:",camino)
