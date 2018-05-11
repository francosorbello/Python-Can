from algo1 import *
from libreriafinal import *

def buscaroad(matriz):
    if matriz[i][j+1]!=1 and matriz[i+1][j]!=1:
        

def imprimirmat(m,n):
	for i in range(0,n):
		print('[ ',end='')
		for j in range(0,n):
			print(m[i][j],'',end='')
		print(']')

matriz=Array(5,Array(5,0))

for a in range(0,5):
    for b in range(0,5):
        matriz[a][b]=1
matriz[0][0]=0
matriz[1][0]=0
matriz[2][0]=0
matriz[3][0]=0
matriz[4][0]=0
matriz[1][1]=0
matriz[1][2]=0
matriz[1][3]=0
matriz[1][4]=0
matriz[2][4]=0
matriz[3][4]=0
matriz[4][4]=0
imprimirmat(matriz,5)