import math

for angle in range(0, 361, 30):
    sin_value = math.sin(math.radians(angle))
    cos_value = math.cos(math.radians(angle))
    print(f"sin({angle:03d}°) = {sin_value:+1.2f}   cos({angle:03d}°) = {cos_value:+1.2f}")