notas = input().split(" ")

n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

media = ((n1 * 2) + (n2 * 3) + (n3* 4) + (n4 * 1)) / 10

if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5.0:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
elif media >= 5.0 or media <= 6.9:
    nota_exame = float(input())
    media_final = (media + nota_exame) /2

    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    print(f"Nota do exame: {nota_exame:.1f}")
    if media_final > 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {media_final}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {media_final}")