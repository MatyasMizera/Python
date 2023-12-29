vyska = 175
vaha = 76
vyska = vyska / 100
bmi = vaha / (vyska * vyska)
if bmi < 18.5:
    print("podváha")
elif bmi > 18.5 and bmi < 24.9:
    print("normální váha")
elif bmi > 24.9 and bmi < 29.9:
     print("Nadváha")
elif bmi > 29.9 and bmi < 34.9:
     print("Obezita 1.stupně")
elif bmi > 34.9 and bmi < 39.9:
     print("Obezita 2.stupně")
elif bmi > 39.9 and bmi < 100:
     print("Obezita 3.stupně")
     