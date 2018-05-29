from algo1 import *
from libreriafinal import *

def clear(lista):
    #vacía una lista
    nodo=lista.head
    nodo.nextNode=None
    nodo.value=None

def calculoranking(lista):
    nodo=lista.head
    aux=0
    while nodo != None:
        aux=aux+nodo.value.value.ranking
        nodo=nodo.nextNode
    return aux

def prometedor(costo,consumo_max):
    if costo>consumo_max:
        return False
    return True

def busco_mejores(appnode,gestor,apps_actual,costo,aux):
    if aux: #aux guarda V si obtuve una solucion viable. Caso contrario es Falsa
        if gestor.ranking_max<calculoranking(apps_actual):
            #si el ranking de la posible solucion es mejor que el que tengo como base
            #la muestro como solucion buena
            print("Solución")
            gestor.ranking_max=calculoranking(apps_actual)
            imprimirAPP2(apps_actual)
            clear(apps_actual)
        else:
            return
    else:
        while appnode != None:
            costo=costo+appnode.value.consumo#obtengo un nuevo costo
            if prometedor(costo,gestor.consumo_max):
                appendLIST(apps_actual,appnode)#guardo las apps que llevo hasta el momento
                busco_mejores(appnode.nextNode,gestor,apps_actual,costo,True)
                #al terminar reinicio el costo restando lo sumado y quito la app agregada
                costo=costo-appnode.value.consumo
                pop(apps_actual)
                print("1")
            else:
                busco_mejores(appnode.nextNode,gestor,apps_actual,costo,False)
            appnode=appnode.nextNode
    return costo

def gestor_apps(lista_apps,consumo_max):
    node=lista_apps.head
    apps_actual=Linkedlist()#lista que contiene las apps utilizadas durante la recursividad
    appendLIST(apps_actual,node)
    costo=node.value.consumo
    node=node.nextNode
    gestor=celular()
    gestor.ranking_max=node.value.ranking
    gestor.consumo_max=consumo_max
    best_app=busco_mejores(node,gestor,apps_actual,costo,False)

def imprimirAPP2(l):
  #imprime una lista
  currentAPP=node()
  currentAPP=l.head
  while currentAPP != None:
    print('[',end='')
    print(currentAPP.value.value.nombre,",",currentAPP.value.value.consumo,",",currentAPP.value.value.ranking,end=']')
    currentAPP=currentAPP.nextNode
  print("")

def imprimirAPP(l):
  #imprime una lista
  currentAPP=node()
  currentAPP=l.head
  while currentAPP != None:
    print('[',end='')
    print(currentAPP.value.nombre,",",currentAPP.value.consumo,",",currentAPP.value.ranking,end=']')
    currentAPP=currentAPP.nextNode
  print("")

def quito_inutiles(lista_apps,consumo_max):
    #elimina las apps que sobrepasen el consumo maximo
    currentnode=lista_apps.head
    while currentnode != None:
        if currentnode.value.consumo>consumo_max:
            deleteAPP(lista_apps,currentnode.value.consumo)
        currentnode=currentnode.nextNode
    return lista_apps

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
print("Lista de apps:")
imprimirAPP(lista_apps)
print("--------")
gestor_apps(lista_apps,consumo_max)