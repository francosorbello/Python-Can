#-VORAZ-#
from libreriafinal import *
from algo1 import *
import time

def app_final(lista_apps,x):
    #busca el nodo que contiene el valor x y lo devuelve
    nodo=lista_apps.head
    while nodo !=None:
        if nodo.value.ranking==x:
            return nodo
        nodo=nodo.nextNode

def decido_mejores(lista_apps,consumo_max):
    current=lista_apps.head
    ranking_base=current.value.ranking
    mejor_app=buscando(current,ranking_base)
    return mejor_app

def buscando(app,ranking_base):
    #busco la app con el mejor ranking 
    if app != None:
        if app.value.ranking>ranking_base:
            #a diferencia de programación dinámica, donde recorro toda la lista,
            #en greedy tomo el primer caso que sea mejor que el caso base
            ranking_base=app.value.ranking
        return buscando(app.nextNode,ranking_base)
    return ranking_base

def deleteAPP(linkedlist,element):
    #borra un elemento de una lista
    currentnode=node()
    currentnode=linkedlist.head
    if currentnode != None:
        if linkedlist.head.value.uso==element:
            linkedlist.head=currentnode.nextNode
        else:
            while currentnode != None:
                if currentnode.nextNode.value.uso == element:
                    currentnode.nextNode=currentnode.nextNode.nextNode
                    return linkedlist
                currentnode=currentnode.nextNode
    else:
        return None

def imprimirAPP(l):
  #imprime una lista
  currentAPP=node()
  currentAPP=l.head
  while currentAPP != None:
    print('[',end='')
    print(currentAPP.value.nombre,",",currentAPP.value.uso,",",currentAPP.value.ranking,end=']')
    currentAPP=currentAPP.nextNode
  print("")

def quito_inutiles(lista_apps,consumo_max):
    #elimina las apps que sobrepasen el consumo maximo
    currentnode=lista_apps.head
    while currentnode != None:
        if currentnode.value.uso>consumo_max:
            deleteAPP(lista_apps,currentnode.value.uso)
        currentnode=currentnode.nextNode
    return lista_apps
  
def gestor_apps(lista_apps,consumo_max):
    lista_apps=quito_inutiles(lista_apps,consumo_max)#elimina las apps que sobrepasen el consumo maximo
    imprimirAPP(lista_apps)
    app=decido_mejores(lista_apps,consumo_max)
    app=app_final(lista_apps,app)
    print("Mejor app:")
    print("[",app.value.nombre,",",app.value.uso,",",app.value.ranking,"]")

class app:
    ranking=None
    uso=None
    nombre=None
class Linkedlist:
    head=None
class node:
    value=None
    nextNode=None

consumo_max=5
print("Consumo máximo:",consumo_max)
lista_apps=Linkedlist()
#HARDCODEO
app1=app()
app1.ranking=4
app1.uso=5
app1.nombre="Facebook"
appendLIST(lista_apps,app1)

app2=app()
app2.ranking=9
app2.uso=8
app2.nombre="Twitter"
appendLIST(lista_apps,app2)

app3=app()
app3.ranking=1
app3.nombre="Mail"
app3.uso=7
appendLIST(lista_apps,app3)

app4=app()
app4.ranking=8
app4.uso=5
app4.nombre="Reddit"
appendLIST(lista_apps,app4)

app5=app()
app5.ranking=6
app5.uso=2
app5.nombre="Ajustes"
appendLIST(lista_apps,app5)

print("[Nombre, USO , RANKING]")
print("---------------")
print("Lista de apps:")
imprimirAPP(lista_apps)
print("--------")
gestor_apps(lista_apps,consumo_max)