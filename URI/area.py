x = input().split(" ")

a = float(x[0])
b = float(x[1])
c = float(x[2])

pi = 3.14159

triangle = (a * c) / 2
circle = pi * (c * c)
trapeze = ((a + b) * c )/ 2
square = b * b
rectangle = a * b

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapeze:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")