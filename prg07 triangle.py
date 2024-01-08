def triangle(h):
    for i in range(1, h + 1):
        print("  " * (h - i), "000 " * (i * 1 - 1),sep="")
    
triangle(10)
