x = int(input("Primeira nota: "))
y = int(input("Segunda nota: "))
z = int(input("Terceira nota: "))

media = (x + y + z) / 3

if media >= 70:
    print("O aluno foi aprovado")
    print(f"Media final: {media:.0f}")
else: 
    print("O aluno foi reprovado")
    print(f"Media final: {media:.0f}")