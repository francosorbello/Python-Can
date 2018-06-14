lista=[12,4,5,3,8,7]
i=0
aux=[]
update=[]
for a in range(0,len(lista)):
    aux.append(lista[a])
    print("aux:",aux)
    #####FALTA ORDENAR AUX####
    if len(aux)%2 !=0:
        #si la lista es de largo impar
        n=len(aux)//2
        update.append(aux[n])
        print("update:",update)
        print("--")
        i+=1
    else:
        n1=len(aux)//2
        n2=len(aux)//2-1
        update.append((aux[n1]+aux[n2])/2)
        print("update:",update)
        print("--")
        i+=1
print(update)
