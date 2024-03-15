def odpočet(n):
    while n > 0:
        yield n
        n -= 1

for i in odpočet(5):
    print(i)
