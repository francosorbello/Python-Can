import time
from algo1 import *
from libreriafinal import *

inicio=time.time()
def fibonacci2(x):
    resultado= [0,1]
    if x<2:
        return(resultado[x])
    else:
        fib=0
        n1=resultado[1]
        n2=resultado[0]
        for n in range(1,x):
            fib=n1+n2
            n2=n1
            n1=fib
    return fib
res=fibonacci2(10)
print("Resultado: ",res)
print("Tiempo: ",(time.time()-inicio))
