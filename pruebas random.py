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
#a[0]=a[0].ljust(4)
#print(len(a[0]))
#eso=busco_max(a)
#print(eso)
#print(relleno(a,eso))
print(a[0][0])
