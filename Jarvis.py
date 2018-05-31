import math

def extraigo_nro(x,mod_val):
    aux=x//mod_val
    aux=aux % 10
    return aux

def insertionSortMod(unsorted_array, index):
    if len(unsorted_array) > 1:
        mod_val = math.pow(10,index-1)
        i = 1
    while i < len(unsorted_array):
        check_val = unsorted_array[i]
        check_val_mod = extraigo_nro(check_val,mod_val)
        j = i - 1
        while j >= 0 and extraigo_nro(unsorted_array[j],mod_val) > check_val_mod:
            unsorted_array[j+1] = unsorted_array[j]
            unsorted_array[j] = check_val
            j -= 1
        i += 1
    print(unsorted_array)
    return unsorted_array

def getNumDigit(n):
    #divido n por 10 hasta que el resultado da 0
    #de esta manera obtengo la cantidad de digitos del numero
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def radixSort(arr, max_value):
    num_digits = getNumDigit(max_value)
    for digit in range(num_digits+1,1,-1):
        arr = insertionSortMod(arr, digit)
    return arr

arr=[76160,7368,43958,39047,27957,98158,76529,93511,87543,51969]
print(arr)
print("Lista (des)ordenada:")
aux=radixSort(arr,98158)
print(aux)
