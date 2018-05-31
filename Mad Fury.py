#LAS FUNCIONES BUSCO_MAX Y RELLENO AGREGAN ESPACIOS A LAS PALABRAS PARA QUE TODAS QUEDEN DEL MISMO
#LARGO. CONVIENE HACER ESO???

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

def insertionSortMod(unsorted_array, index):
    if len(unsorted_array) > 1:
        i = 1
    while i < len(unsorted_array):
        check_val = unsorted_array[i]
        n=busco_max(unsorted_array)-i#empiezo en la ultima letra
        check_val_mod = check_val[n]
        j = i - 1
        while j >= 0 and  unsorted_array[j][n] > check_val_mod:
            unsorted_array[j+1] = unsorted_array[j]
            unsorted_array[j] = check_val
            j -= 1
        i += 1
    print(unsorted_array)
    return unsorted_array

def radixSort(arr, max_value):
    for digit in range(1,max_value+1):
        arr = insertionSortMod(arr, digit)
    return arr

nombres=["viuda negra","caballero negro","she-hulk","bestia","starfox","madame máscara","hulk","visión","ms. marvel","bruja escarlata"]
print("Lista desordenada:")
print(nombres)
print("----")
nombres=agrego_espacios(nombres)
radixSort(nombres,busco_max(nombres))
print("Lista ordenada:")
print(nombres)