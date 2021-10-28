valor_total = float(input("Digite o valor total a financiar: "))
taxa_juros = float(input("Digite a taxa de juros (%ao mes): "))
parcelas = float(input("Digite a quantidade de parcelas: "))
taxa_adm = float(input("Digite a taxa de administracao (R$/mes): "))

cf = ( taxa_juros / 100) / ( 1- ( 1+ ( taxa_juros / 100 ) ) ** ( -parcelas ) )

prestacao = (valor_total * cf)+(taxa_adm)
resultado = (prestacao * parcelas)
print(f"O valor da parcela e: R${prestacao:.2f}")
print(f"O valor total a ser pago sera de: R${resultado:.2f}")