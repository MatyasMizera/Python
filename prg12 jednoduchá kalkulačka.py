číslo1 = float(input("První číslo: "))
operace = input("operace (+, -, *, /): ")
číslo2 = float(input("druhý číslo: "))
výsledek = 0
if operace == '+':
    výsledek = číslo1 + číslo2
elif operace == '-':
    výsledek = číslo1 - číslo2
elif operace == '*':
    výsledek = číslo1 * číslo2
elif operace == '/':
    výsledek = číslo1 / číslo2
print(f"výsledek: {výsledek}")