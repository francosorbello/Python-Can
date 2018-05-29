from random import randint 
def respuestas(x):
    if x=="si" or x=="Si" or x=="SI":
        return True
    elif x=="no" or x=="No" or x=="NO":
        return False
    else:
        print("Error: ingrese una respuesta correcta")

def check_primo(nro): 
    for a in range(2,nro):
        if mcd(nro,a)!=1:
            return False
    return True
            
def division(numerador,denominador):
    sol=2*[0] #sol es un vector que contiene el denominador y el numerador simplificado
    if numerador>=denominador:
        div=mcd(numerador,denominador)
    else:
        div=mcd(denominador,numerador)
    sol[0]=numerador//div
    sol[1]=denominador//div
    #print("Fracción simplificada: ",numerador,"/",denominador)
    return sol

def mcd(r0,r1,aux=0):
    if r1==0:
        return aux
    else:
        aux=r1
        return mcd((r0//r1)*r1,(r0%r1),aux)

#--SIMPLIFICAR FRACCIÓN--#
#creo una fracción random
numerador=randint(1,50)
denominador=randint(1,50)
solucion=division(numerador,denominador)
#el user ingresa su respuesta
aux=1
while aux!=0:
    print("Simplifique:")
    print(numerador,"/",denominador)
    numerador=int(input("Ingrese numerador: "))
    denominador=int(input("Ingrese denominador: "))
    if solucion[0]==numerador and solucion[1]==denominador:
        print("Respuesta correcta.")
        break
    else:
        print("Respuesta incorrecta. Intente de nuevo.")
print("-------------------")
#--NUMERO PRIMO--#
nro=randint(1,50)
solucion=check_primo(nro)
aux=1
while aux!=0:
    print(nro,"es primo?")
    soluser=input("Ingrese 'si' o 'no':")
    aux2=respuestas(soluser)
    if aux2==solucion:
        print("Respuesta correcta.")
        break
    else:
        print("Respuesta incorrecta. Intente de nuevo.")
        print("------")
        