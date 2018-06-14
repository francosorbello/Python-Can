hash={}
lista=[1,2,3,"perro","perro",6,7]
for i in range(0,len(lista)):
    if lista[i]=="perro":
        break
hash["perro"]=i
print(hash)
print(hash["perro"])
del hash["perro"]
#print(hash["perro"])
print(hash)