num = input().split(" ")
account = 0

hour_ini = int(num[0])
hour_fin = int(num[1])

if hour_ini < hour_fin:
    account = hour_fin - hour_ini
else:
    account = (24 - hour_ini) + hour_fin

print(f"O JOGO DUROU {account} HORA(S)")