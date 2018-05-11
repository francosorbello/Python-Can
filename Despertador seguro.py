def check_primo(nro):
    #PREGUNTAR SI ESTÁ BIEN. LA COMPLEJIDAD VA A SER MAYOR A SI SOLO HAGO UN BUCLE
    for a in range(2,nro):
        if mcd(nro,a)!=1:
            print("No es primo.")
            return
    print("Es primo.")
    return
            
def division(numerador,denominador):
    if numerador>=denominador:
        div=mcd(numerador,denominador)
    else:
        div=mcd(denominador,numerador)
    numerador=numerador//div
    denominador=denominador//div
    print("Fracción simplificada: ",numerador,"/",denominador)
    return (numerador/denominador)

def mcd(r0,r1,aux=0):
    if r1==0:
        return aux
    else:
        aux=r1
        return mcd((r0//r1)*r1,(r0%r1),aux)

#--SIMPLIFICAR FRACCIÓN--#
numerador=int(input("Ingrese numerador: "))
denominador=int(input("Ingrese denominador: "))
print(division(numerador,denominador))
#--NUMERO PRIMO--#
nro=int(input("Ingrese numero a checkear: "))
check_primo(nro)