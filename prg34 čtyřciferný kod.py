#musí to být dohromadi 13
#musí to být vzestupně
for a in range(9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                if a < b and b < c and c < d:
                    if (a + b + c + d) == 13:
                            print(f"{a}{b}{c}{d}")