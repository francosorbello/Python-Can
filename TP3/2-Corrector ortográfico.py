from algo1 import *

def check_contraseña(tolerancia,pass_original,password):
    aux=Levenshtein(pass_original,password)
    if aux<=tolerancia:
        print("Contraseña correcta.")
    else:
        print("Contraseña incorrecta.")
    return

def imprimirMAT(matriz,m,n):
    for i in range(0,m):
        for j in range(0,n):
            #print('[',end='')
            print("[",matriz[i][j],end=']')
        print("")

def Levenshtein(pass_original,password):
    len_base=len(pass_original)+1#len_base contiene el largo de la contraseña original+1
    len_pass=len(password)+1#len_pass contiene el largo de la contraseña a comparar+1
    dist=Array(len_base,Array(len_pass,0))#dist es la matriz que contiene las distancias
    for i in range(0,len_base):
        dist[i][0]=i
    for j in range(0,len_pass):
        dist[0][j]=j
    for i in range(1,len_base):
        for j in range(1,len_pass):
            if pass_original[i-1]==password[j-1]:
                cost=0
            else:
                cost=1
            dist[i][j]=min(dist[i-1][j]+1 , dist[i][j-1]+1 ,dist[i-1][j-1] + cost)
    return dist[len_base-1][len_pass-1]

tolerancia=int(input("Ingrese el nivel de cercanía tolerable: "))
pass_original=input("Ingrese la contraseña original: ")
password=input("Ingrese la contraseña: ")
#Mis casos base son la contraseña original y la que está ingresando el usuario actualmente
check_contraseña(tolerancia,pass_original,password)