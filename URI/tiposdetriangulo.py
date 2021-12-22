n = input().split(" ")

a = float(n[0])
b = float(n[1])
c = float(n[2])

if (a >= (b + c)):
    print("NAO FORMA TRIANGULO")
elif ((a**2) == ((b**2) + (c**2))):
    print("TRIANGULO RETANGULO")
elif ((a**2) > ((b**2) + (c**2))):
    print("TRIANGULO OBTUSANGULO")
elif ((a**2) < ((b**2) + (c**2))):
    print("TRIANGULO ACUTANGULO")
elif (a == b and a == c):
    print("TRIANGULO EQUILATERO")
elif (a == b or a == c or b == c):
    print("TRIANGULO ISOSCELES")
