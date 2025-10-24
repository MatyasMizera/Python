n = int(input("Zadej celé číslo větší než 0:"))

pocet_sudych = 0
pocet_lichych = 0
pocet_prvocisel = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "- sudé", end=", ")
        pocet_sudych += 1
    else:
        print(i, "- liché", end=", ")
        pocet_lichych += 1

    
    if i % 3 == 0:
        print("dělitelné 3,", end=" ")
    else:
        print("nedělitelné 3,", end=" ")

    
    je_prvocislo = True
    if i < 2:
        je_prvocislo = False
    else:
        for j in range(2, i):
            if i % j == 0:
                je_prvocislo = False
                break

    if je_prvocislo:
        print("prvočíslo")
        pocet_prvocisel += 1
    else:
        print("není prvočíslo")

print("Sudých čísel:", pocet_sudych)
print("Lichých čísel:", pocet_lichych)
print("Prvočísel:", pocet_prvocisel)
