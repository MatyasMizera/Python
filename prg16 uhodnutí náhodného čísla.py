import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Tipni si číslo od 1 do 10: "))
    
    if guess == secret_number:
        print("Správně! Uhodl si číslo!")
        break
    else: 
        print("Špatné číslo, zkus to znovu")