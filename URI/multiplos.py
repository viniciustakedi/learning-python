n = input().split(" ")
a = int(n[0])
b = int(n[1])
account = 0 

if a > b:
    account = a / b
else:
    account = b / a

if account % 2 == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
