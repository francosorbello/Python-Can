lower_c={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"}
upper_c={"A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
numbers={0,1,2,3,4,5,6,7,8,9}
cadena=input("Ingrese palabra: ")
i=0
aux=0

while cadena[i] in lower_c:
    i+=1
    if i==len(cadena):
        aux=1
        break

if aux==1:
    print("Es valido")
else:
    print("Es invalido")

#print("a" in lower_c)