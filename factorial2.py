def factorial(n):
    if n <= 1:
        return 1
    else:
        return(n*factorial(n-1))
    
def recursiva1(n):
    if n<=1:
        return 1
    else:
        return recursiva1(n-1)+recursiva1(n-1)

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

x=int(input("Ingrese numero: "))
start=int(input("1. Factorial - 2.Recursiva 1 - 3.Recursiva3 - 4. Recursiva4 - 5. Fibonacci: "))
if start==1:
    res=factorial(x)
elif start==2:
    res=recursiva1(x)
elif start==3:
    res=recursiva3(x)
elif start==5:
    res=fibonacci(x)
else:
    res=recursiva4(x)
print("Resultado: ",res)
