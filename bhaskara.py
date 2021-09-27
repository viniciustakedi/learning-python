import math

x = input().split(" ")

a = float(x[0])
b = float(x[1])
c = float(x[2])

triangle = (b * b) - (4 * a * c)

if triangle <= 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(triangle)) / (2 * a)
    x2 = (-b - math.sqrt(triangle)) / (2 * a)

    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")