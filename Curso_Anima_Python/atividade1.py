valor_compra = 637.86 #valor total da compra
n_cinquenta = 10 #quantidade de notas de 50 reais
n_dez = 12 #quantidade de notas de 10 reais
n_cinco = 4 #quantidade de notas de 5 reais

valor_recebido = (n_cinquenta * 50) + (n_dez * 10) + (n_cinco * 5) #conta para somar todas as notas e descobrir o valor final
troco = valor_recebido - valor_compra #conta para descobrir o troco

#prints para visualização final
print("Sua compra ficou em R$"+str(valor_compra))
print(f"Voce foneceu:\n{n_cinquenta} de R$50,00\n{n_dez} de R$10,00\n{n_cinco} de R$5,00\ntotalizando R${valor_recebido}")
print(f"Seu troco e R${troco:.2f}. Obrigado!")
