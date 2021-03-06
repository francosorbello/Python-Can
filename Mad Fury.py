# El parámetro es un caracter y devuelve un número
def numberFromChar(c):
    chars = {
        '\x00': 0,
        ' ': 1,
        '-': 2,
        '.': 3,
        "'": 4,
        'a': 5,
        'á': 6,
        'b': 7,
        'c': 8,
        'd': 9,
        'e': 10,
        'é': 11,
        'f': 12,
        'g': 13,
        'h': 14,
        'i': 15,
        'í': 16,
        'j': 17,
        'k': 18,
        'l': 19,
        'm': 20,
        'n': 21,
        'o': 22,
        'ó': 23,
        'p': 24,
        'q': 25,
        'r': 26,
        's': 27,
        't': 28,
        'u': 29,
        'ú': 30,
        'v': 31,
        'w': 32,
        'x': 33,
        'y': 34,
        'z': 35
    }
    return chars[c]

def imprimir(lista):
    #imprime una lista
    for a in range(0,len(lista)):
        print("[",lista[a],"]")

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
    #agrega espacios a las palabras para que todas queden del mismo largo
    for a in range(0,len(lista)):
        if len(lista[a])<max:
            lista[a]=lista[a].ljust(max," ")#agrego los espacios faltantes
    return lista

def insertionSortMod(unsorted_array, index, max_value):
    if len(unsorted_array) > 1:
        i = 1
    while i < len(unsorted_array):
        check_val = unsorted_array[i]
        n=max_value-index #empiezo en la ultima letra
        #aprovecho que python permite extraer un caracter de una palabra para compararlas
        check_val_mod = numberFromChar(check_val[n])
        j = i - 1
        while j >= 0 and numberFromChar(unsorted_array[j][n]) > check_val_mod:
            unsorted_array[j+1] = unsorted_array[j]
            unsorted_array[j] = check_val
            j -= 1
        i += 1
    return unsorted_array

def radixSort(arr, max_value):
    for digit in range(1,max_value+1):
        arr = insertionSortMod(arr, digit,max_value)
    return arr
caracteres={}
nombres=["torunn","sentry","moonstone","avispa","phil coulson","quicksilver","kate bishop","luke cage","ex nihilo","ojo de halcón","gata infernal","crystal","máquina de guerra","henry peter gyrich","rick jones","wolverine","t'chaka","edwin jarvis","capitán marvel","namor","silverclaw","spider-man","white tiger","carol danvers","viper","espadachín","thor","zabu","iron man","defensor","nick fury","pantera negra","falcon","mantis","monica rambeau","henry pym","capitán britania","hércules","gravitón","sharon carter","venom","wiccan","ant-man","capitán américa","hombre hormiga","hombre maravilla","pepper potts","maria hill"]
nombres=agrego_espacios(nombres)
print("Lista desordenada:")
imprimir(nombres)
print("\n")
radixSort(nombres,busco_max(nombres))
print("Lista ordenada:")
imprimir(nombres)
