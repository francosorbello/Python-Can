def devuelvo_posicion(x,cant_estantes,cant_productos,n):
    #devuelve la estanteria y el estante en el que se encuentra
    #un producto basado en su posicion en la lista
    estanteria=0
    aux=cant_productos*cant_estantes
    for i in range(0,n+1,aux):
        if i>=x:
            print("Estanteria ",estanteria)
            break 
        estanteria+=1
    estante=0
    for a in range((estanteria-1)*aux,i+1,producto):
        #reduzco la búsqueda a la estantería donde esta el producto
        if a>=x:
            print("Estante ",estante)
            break
        estante+=1

lista=250*[0]
estanteria=5
estante=5
producto=10
x=25
devuelvo_posicion(x,estante,producto,len(lista))
"""aux=0
for i in range(0,len(lista)+1,producto*estante):
    if i>=x:
        print("Estanteria ",aux)
        break 
    aux+=1
aux2=0
for a in range((aux-1)*estante*producto,i+1,producto):
    if a>=x:
        print("Estante ",aux2)
        break
    aux2+=1"""
