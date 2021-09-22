horas = input()
velocidade = input()
gasto_litro = 12

account = (int(horas) * int(velocidade)) / gasto_litro

print(round(account, 3))