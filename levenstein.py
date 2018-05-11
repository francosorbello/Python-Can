from algo1 import *

def imprimirMAT(matriz,m,n):
    for i in range(0,m):
        for j in range(0,n):
            #print('[',end='')
            print("[",matriz[i][j],end=']')
        print("")

str1="casa"
str2="asa"
lenstr1=len(str1)+1
lenstr2=len(str2)+1
dist=Array(lenstr1,Array(lenstr2,0))

for i in range(0,lenstr1):
    dist[i][0]=i
for j in range(0,lenstr2):
    dist[0][j]=j

for i in range(1,lenstr1):
    for j in range(1,lenstr2):
        if str1[i-1]==str2[j-1]:
            cost=0
        else:
            cost=1
        dist[i][j]=min(dist[i-1][j]+1 , dist[i][j-1]+1 ,dist[i-1][j-1] + cost)

imprimirMAT(dist,len(str1)+1,len(str2)+1)
print(dist[len(str1)][len(str2)])