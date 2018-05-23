from libreriafinal import *
from algo1 import *
import time

def imprimirAPP(l):
  #imprime una lista
  currentAPP=node()
  currentAPP=l.head
  while currentAPP != None:
    print('[',end='')
    print(currentAPP.value.nombre,",",currentAPP.value.uso,",",currentAPP.value.ranking,end=']')
    currentAPP=currentAPP.nextNode
  print("")

def decido_apps(lista_apps,consumo_apps):
    currentapp=lista_apps.head
    mejorapp=currentapp.value #tomo la primer app como la mejor app base
    currentapp=currentapp.nextNode
    while currentapp != None:
        #si la siguiente app tiene mejor ranking y consume menos del maximo, actualizo el caso base 
        if currentapp.value.ranking>mejorapp.ranking and currentapp.value.uso<consumo_apps:
            mejorapp=currentapp.value
        currentapp=currentapp.nextNode
    return mejorapp
    
def gestor_apps(lista_apps,consumo_max):
    print("Consumo máximo: ",consumo_max)
    print("LISTA SIN ORDENAR:")
    imprimirAPP(lista_apps)
    best=decido_apps(lista_apps,consumo_max)
    print("---------------")
    print("MEJOR APP:")
    print("[",best.nombre,",",best.uso," , ",best.ranking,"]")

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
lista_apps=Linkedlist()
#HARDCODEO
app1=app()
app1.ranking=5
app1.uso=1
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
app4.ranking=5
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