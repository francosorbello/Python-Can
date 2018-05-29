from algo1 import *
from libreriafinal import *

def recursiva(nodo,lista,aux):
    while nodo != None:
        name=nodo.value.nombre
        if aux!=nodo.value.nombre:
            appendLIST(lista,nodo)
            imprimirAPP(lista)
            recursiva(nodo.nextNode,lista,aux)
            pop(lista)
        nodo=nodo.nextNode
         

def imprimirAPP(l):
  #imprime una lista
  currentAPP=node()
  currentAPP=l.head
  while currentAPP != None:
    print('[',end='')
    print(currentAPP.value.value.nombre,",",currentAPP.value.value.consumo,",",currentAPP.value.value.ranking,end=']')
    currentAPP=currentAPP.nextNode
  print("")

def clear(lista):
    nodo=lista.head
    nodo.nextNode=None
    nodo.value=None

class celular:
    consumo_max=None
    ranking_max=None

class app:
    ranking=None
    consumo=None
    nombre=None
class Linkedlist:
    head=None
class node:
    value=None
    nextNode=None

consumo_max=19
print("Consumo máximo:",consumo_max)
lista_apps=Linkedlist()
#HARDCODEO
app1=app()
app1.ranking=4
app1.consumo=5
app1.nombre="Facebook"
appendLIST(lista_apps,app1)

app2=app()
app2.ranking=9
app2.consumo=8
app2.nombre="Twitter"
appendLIST(lista_apps,app2)

app3=app()
app3.ranking=1
app3.nombre="Mail"
app3.consumo=7
appendLIST(lista_apps,app3)

app4=app()
app4.ranking=8
app4.consumo=5
app4.nombre="Reddit"
appendLIST(lista_apps,app4)

app5=app()
app5.ranking=6
app5.consumo=2
app5.nombre="Ajustes"
appendLIST(lista_apps,app5)

print("[Nombre, consumo , RANKING]")
print("---------------")
"""print("Lista de apps:")
imprimirAPP(lista_apps)
print("--------")"""


lista=LinkedList()
nodo=lista_apps.head
nodo2=lista_apps.head
while nodo != None:
    appendLIST(lista,nodo)
    recursiva(nodo2,lista,nodo.value.nombre)
    imprimirAPP(lista)
    print("--")
    lista.head=None
    nodo=nodo.nextNode
