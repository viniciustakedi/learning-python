salario = float(input())

if salario <= 400:
    porcentagem = "15%"
    reajuste = salario * 0.15
    novo_salario = reajuste + salario

elif 400.01 <= salario <= 800.00:
    porcentagem = "12%"
    reajuste = salario * 0.12
    novo_salario = reajuste + salario

elif 800.01 <= salario <= 1200.00:
    porcentagem = "10%"
    reajuste = salario * 0.1
    novo_salario = reajuste + salario

elif 1200.01 <= salario <= 2000.00:
    porcentagem = "7%"
    reajuste = salario * 0.07
    novo_salario = reajuste + salario

elif salario > 2000.00:
    porcentagem = "4%"
    reajuste = salario * 0.04
    novo_salario = reajuste + salario

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print("Em percentual: "+porcentagem)