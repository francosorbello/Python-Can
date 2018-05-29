from libreriafinal import *
from algo1 import *
import time

def dinamica(n,k):
    casobase=[1,1]
    if n==1 and k==1:
        return 1
    else:
        resultados=Array(n+1,Array(n+1,0))
        for a in range(0,n+1):
            for b in range(0,k+1):
                if b==0 or a==b:
                    resultados[a][b]=1
                elif a>b:
                    aux1=resultados[a-1][b-1]
                    aux2=resultados[a-1][b]
                    resultados[a][b]= aux1+aux2         
        aux=resultados[n][k]
        return aux
                
def combinacional(n,k):
    res= factorial(n)/(factorial(k)*factorial(n-k))
    return res

def factorial(numero):
    resultado=[1]
    if numero<3:
        return numero
    else:
        rta=1
        n1=resultado[0]
        for n in range(0,numero):
            rta=n1*rta
            n1=n1+1
    return rta

cant_pictogramas=int(input("Ingrese la cantidad de pictogramas disponibles: "))
largo_pass=int(input("Ingrese el largo de la contraseña: "))

if cant_pictogramas<largo_pass:
    print("Error: el largo de la contraseña tiene que ser menor o igual a la cantidad de pictogramas.")
    while cant_pictogramas<largo_pass:
        cant_pictogramas=int(input("Ingrese la cantidad de pictogramas disponibles: "))
        largo_pass=int(input("Ingrese el largo de la contraseña: "))
        print("Error: el largo de la contraseña tiene que ser menor o igual a la cantidad de pictogramas.")

#parte gráfica
aux=int(input("1.Calcularlo con 'divide y vencerás'\n2.Calcular con 'programación dinámica'\n3.Comparar tiempo de ejecución.\n "))
if aux==1:
    tiempo=combinacional(cant_pictogramas,largo_pass)*1.3
    print("Tiempo de acceso por fuerza bruta:",tiempo,"segundos")
elif aux==2:
    tiempo=dinamica(cant_pictogramas,largo_pass)
    print("Tiempo de acceso por fuerza bruta:",tiempo,"segundos")
else:
    start=time.time()
    tiempo=combinacional(cant_pictogramas,largo_pass)*1.3
    fin=time.time()
    tiempoDV=fin-start
    print("Tiempo de ejecución divide y vencerás: ",tiempoDV)
    #---#
    start=time.time()
    tiempo=dinamica(cant_pictogramas,largo_pass)
    fin=time.time()
    tiempoDIN=fin-start
    print("Tiempo de ejecución dinámica: ",tiempoDIN)