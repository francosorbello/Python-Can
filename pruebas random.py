def vacio(lista,max):
    max=(-1)*max
    for a in range(0,len(lista)):
        lista[a]=lista[a].ljust(100*max)
    return lista


def busco_max(lista):
    max=len(lista[0])
    for a in range(0,len(lista)):
        if len(lista[a])>max:
            max=len(lista[a])
    return max
def relleno(lista,max):
    for a in range(0,len(lista)):
        if len(lista[a])<max:
            lista[a]=lista[a].rjust(max," ")#agrego los espacios faltantes
    return lista

a=["hola","parasito"]
a=relleno(a,busco_max(a))
print(vacio(a,busco_max(a)))