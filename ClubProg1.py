def separo(lista,i,j,x):
    if j+1<=len(lista):
        if lista[i]+lista[j]==x:
            return True
        else:
            separo(lista,i,j+1,x)
        return False

A=5*[0]
x=6
#relleno la matriz
for a in range(0,5):
    A[a]=a+1
print(A)
print("x:",x)
#main()
for a in range(0,5):
    aux=separo(A,a,0,x)
print(aux)