a = float(input())
b = float(input())
c = float(input())
d = float(input()) 
e = float(input())
f = float(input())

numeros = [a, b, c, d, e, f]

indicador = 0
positivos = 0
while indicador < 6:
    num = float(numeros[0])
    if num > 0:
        positivos += 1
    indicador += 1

print(f"{positivos:.1f} valores positivos")
