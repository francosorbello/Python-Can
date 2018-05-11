import time

def fibonacci(x):
    if x==1:
        return 1
    elif x==0:
        return 0
    elif x<0:
        return None
    else:
        sol=fibonacci(x-1)+fibonacci(x-2)
    return sol
inicio=time.time()
a=fibonacci(888)
print("fibonacci: ",a)
print("Tiempo: ",time.time()-inicio)