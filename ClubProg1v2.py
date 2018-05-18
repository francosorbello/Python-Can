def largo(lista):
    if len(lista)%2!=0:
        return len(lista)//2+1
    return len(lista)//2

def sumo(lista,x):
    if lista[0]+lista[1]==x:
        return True
    return False

def comparo(lista,lizq,lder):
    a=0
    if a==0:
        return 

def sublist(lista,inicio,fin):
    aux=largo(lista)
    nuevalista=aux*[0]
    aux2=0
    if inicio !=0:
        aux2=inicio
    #print("[",aux,inicio,fin,"]")
    for a in range(inicio,fin):
        nuevalista[a-aux2]=lista[a]
    return nuevalista

def merge(lista,x):
    largo=len(lista)
    if largo>1:
        lizq=sublist(lista,0,largo//2)
        lder=sublist(lista,largo//2,largo)
        merge(lizq,x)
        merge(lder,x)
        #comparo(lista,lizq,lder)
    return sumo(lista,x)

A=5*[0]
x=6
#relleno la matriz
for a in range(0,5):
    A[a]=a+1
print(A)
print("x:",x)
merge(A,x)
