#Náročná verze
def fibrek(n):
    print("x", end="-")
    if n <= 1:
        return n
    return fibrek(n - 1) + fibrek(n - 2)
#print(fibrek(25))

#Optimalizovaná verze
def fib(n):
    if n <= 1:
        return n
    prev = 0
    fib = 1
    for i in range(2,n + 1):
        fib, prev = fib + prev, fib
    return fib


print(fib(25))