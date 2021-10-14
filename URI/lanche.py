n1, n2 = input().split(" ")

prices = [4.00, 4.50, 5.00, 2.00, 1.50]
account = prices[int(n1)-1] * int(n2)

print(f"Total: R$ {account}0")