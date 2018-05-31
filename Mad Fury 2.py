
def agrego_espacios(lista):
    #esta función deja a todas las palabras del mismo largo agregando espacios en los lugares faltantes
    aux=busco_max(lista)
    relleno(lista,aux)
    return lista

def busco_max(lista):
    #busca la palabra mas larga y devuelve su largo
    max=len(lista[0])
    for a in range(0,len(lista)):
        if len(lista[a])>max:
            max=len(lista[a])
    return max

def relleno(lista,max):
    for a in range(0,len(lista)):
        if len(lista[a])<max:
            lista[a]=lista[a].rjust(max,".")#agrego los espacios faltantes
    return lista

def sorting(lista,index):
    i=1
    while i<len(lista):    
        word=lista[index]
        n=busco_max(lista)
        word_letra=word[n]-i
        while n>=0 and word_letra < lista[n][]

def radixsort(lista):
    n=busco_max(lista)
    for a in range(0,n):
        lista=sorting(lista,n)
    return lista

nombres=["viuda negra","caballero negro","she-hulk","bestia","starfox","madame máscara","hulk","visión","ms. marvel","bruja escarlata"]
