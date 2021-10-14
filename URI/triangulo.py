v = input().split(" ")

a = float(v[0])
b = float(v[1])
c = float(v[2])

area_trapezio = ((a + b) * c) / 2
perimetro_triangulo = a + b + c

if (b-c) < a and a < (b+c):
    if (a-c) < b and b < (a+c):
        if (a-b) < c and c < (a+b):
            print(f"Perimetro = {perimetro_triangulo:.1f}")
        else:
            print(f"Area = {area_trapezio:.1f}")
    else:
        print(f"Area = {area_trapezio:.1f}")
else:
    print(f"Area = {area_trapezio:.1f}")

