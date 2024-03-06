def cisla(a, b):
    while b != 0:
        a, b = b, a % b
    return a

cislo1 = int(input("První číslo: "))
cislo2 = int(input("Druhé číslo: "))

print("Největší společný dělitel je:", cisla(cislo1, cislo2))