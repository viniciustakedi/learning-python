n0 = int(input())
n1 = int(input())
n2 = int(input())
n3 = int(input()) 
n4 = int(input())

pares = 0

pares = pares + 1 if n0 % 2 == 0 else 0
pares = pares + 1 if n1 % 2 == 0 else 0
pares = pares + 1 if n2 % 2 == 0 else 0
pares = pares + 1 if n3 % 2 == 0 else 0
pares = pares + 1 if n4 % 2 == 0 else 0

print(f"{pares} valores pares")
