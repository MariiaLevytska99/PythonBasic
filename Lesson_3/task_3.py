import math

a = float(input("Введіть a "))
b = float(input("Введіть b "))
c = float(input("Введіть c "))

D = b**2 - 4 * a * c

print(f"Дискримінант дорівнює {D}")

if D > 0:
    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a
    print("x1 = " + x1)
    print("x2 = " + x2)
else:
    x = -b / 2 * a
    print("x = " + x)