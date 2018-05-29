# -*- coding: utf-8 -*-

global c
c = 0

def prometedor (A,k):
#Precondición A ya es k-1  prometedor
    for j in range (1,k):
        if A[j]==A[k] or abs(A[j]-A[k]) == abs(k-j):
            return False
    return True


def reinas(A,k,n):
    global c
    c = c + 1
    if k == n:
        if prometedor(A,k):
            print (A)
        else: return
    else:
        for j in range (1,n+1):
            if prometedor (A,k):
                A[k+1]=j
                reinas(A,k+1,n)
            
L = 9*[0]
reinas(L,0,8)



    
    