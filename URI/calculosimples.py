x = input().split(" ")
y = input().split(" ")

code_one = int(x[0]) 
amount_one = int(x[1]) 
price_one = float(x[2]) 

code_two = int(y[0]) 
amount_two = int(y[1]) 
price_two = float(y[2]) 

account_clothes_one = amount_one * price_one
account_clothes_two = amount_two * price_two
account_total = account_clothes_one + account_clothes_two

print(f"VALOR A PAGAR: R$ {account_total:.2f}")
