#-PROGRAMACION DINAMICA-#
from algo1 import *
from libreriafinal import *

def accessAPP(lista,pos):
    #accede a la posicion "pos" de la lista ingresada
    n=lengthLIST(lista)
    app=lista.head
    posaux=0
    while app != None:
        if posaux==pos:
            return app
        posaux+=1
        app=app.nextNode
def decido_apps(matriz,consumo_max):
    #busco el mínimo en una matriz y devuelvo la posición de ese elemento
    n=len(matriz)
    min=matriz[0][0]
    fila=0
    colum=0
    for i in range(0,n):
        for j in range(0,n):
            if matriz[i][j]>min and matriz[i][j]<=consumo_max:
                min=matriz[i][j]
                fila=i
                colum=j
    aux=2*[0]
    aux[0]=fila
    aux[1]=colum
    return aux


def gestor_apps(lista_apps,consumo_max):
    m=genero_matriz(lista_apps)
    mejores_apps=decido_apps(m,consumo_max)
    if mejores_apps[0]==mejores_apps[1]:
        app_final=accessAPP(lista_apps,mejores_apps[0])
        print("Aplicación sobreviviente:")
        print("[",app_final.value.nombre,",",app_final.value.consumo,",",app_final.value.ranking,"]")
    else:
        app_final=2*[0]
        app_final[0]=accessAPP(lista_apps,mejores_apps[0])
        app_final[1]=accessAPP(lista_apps,mejores_apps[1])
        print("Aplicaciones sobrevivientes:")
        print("[",app_final[0].value.nombre,",",app_final[0].value.consumo,",",app_final[0].value.ranking,"]")
        print("[",app_final[1].value.nombre,",",app_final[1].value.consumo,",",app_final[1].value.ranking,"]")
        

def genero_matriz(lista_apps):
    n=lengthLIST(lista_apps) #calculo el largo de la lista
    mat_apps=Array(n,Array(n,0))#genero una matriz que contiene la suma de los consumos de las apps
    #ej: en la pos 2,3 voy a tener el consumo de la app 3 + el consumo de la app 4
    nodobase=lista_apps.head #para hacer la matriz, utilizo el consumo de cada app como caso base
    nodo=lista_apps.head #con esta variable recorro la lista
    for i in range(0,n):
        caso_base=nodobase.value.consumo #tomo el consumo como caso base
        for j in range(0,n):
            if i!=j:
                #si no estoy en la posicion de la app base, sumo con las otras apps
                mat_apps[i][j]=caso_base+nodo.value.consumo
            else:
                #caso contrario, no sumo nada(o sumo por 0)
                mat_apps[i][j]=caso_base
            nodo=nodo.nextNode
        nodo=lista_apps.head #reinicio la var con la que recorro la lista
        nodobase=nodobase.nextNode #paso a la siguiente app y la consumo como caso base
    imprimirMAT(mat_apps,n,n)
    print("")
    return mat_apps

def deleteAPP(linkedlist,element):
    #borra un elemento de una lista
    currentnode=node()
    currentnode=linkedlist.head
    if currentnode != None:
        if linkedlist.head.value.consumo==element:
            linkedlist.head=currentnode.nextNode
        else:
            while currentnode != None:
                if currentnode.nextNode.value.consumo == element:
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
    print(currentAPP.value.nombre,",",currentAPP.value.consumo,",",currentAPP.value.ranking,end=']')
    currentAPP=currentAPP.nextNode
  print("")

class app:
    ranking=None
    consumo=None
    nombre=None
class Linkedlist:
    head=None
class node:
    value=None
    nextNode=None

consumo_max=15
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
app5.consumo=21
app5.nombre="Ajustes"
appendLIST(lista_apps,app5)

print("[Nombre, consumo , RANKING]")
print("---------------")
print("Lista de apps:")
imprimirAPP(lista_apps)
print("--------")
gestor_apps(lista_apps,consumo_max)
