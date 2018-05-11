from libreriafinal import *
from algo1 import *
import time

def orden_uso(l):
    currentnode=node()
    currentnode=l.head
    large=lengthLIST(l)-1 #largo de la lista
    aux=0
    while large > aux:
        while currentnode.nextNode != None:
            if currentnode.value.uso>currentnode.nextNode.value.uso:
                aux2=currentnode.value.uso #guardo el valor en una variable auxiliar
                currentnode.value.uso=currentnode.nextNode.value.uso
                currentnode.nextNode.value.uso=aux2
                continue
            currentnode=currentnode.nextNode
        aux=aux+1
    return l
    
def gestor_apps(lista_apps,consumo_max):
    orden_uso(lista_apps)#devuelve la lista ordenada segun el uso

class app:
    ranking=None
    uso=None
class Linkedlist:
    head=None
class node:
    value=None
    nextNode=None

consumo_max=5
lista_apps=Linkedlist()
#HARDCODEO
app1=app()
app1.ranking=5
app1.uso=1
appendLIST(lista_apps,app1)

app2=app()
app2.ranking=9
app2.uso=8
appendLIST(lista_apps,app2)

app3=app()
app3.ranking=1
app3.uso=7
appendLIST(lista_apps,app3)

app4=app()
app4.ranking=5
app4.uso=5
appendLIST(lista_apps,app4)

app5=app()
app5.ranking=6
app5.uso=2
appendLIST(lista_apps,app5)
gestor_apps(lista_apps,consumo_max)