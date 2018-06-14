def sublist(lista,start,fin):
    sub=[]
    for i in range(start,fin):
        sub.append(lista[i])
    return sub


def binary_search(lista,elem):
    if len(lista)>1:
        return lista[0]
    else:
        mitad=len(lista)//2
        if elem=<lista[mitad]:
            list_left=sublist(lista,0,mid-1)
            binary_search(list_left,elem)
        else:
            list_der=sublist(lista,mid,len(lista))
            binary_search(list_der,elem)            
        


lista=[1,2,3,4,5,6,7,8,9,10]
binary_search