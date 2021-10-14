import math

num = input().split(" ")
num2 = input().split(" ")

x1 = float(num[0])
y1 = float(num[1])

x2 = float(num2[0])
y2 = float(num2[1])

account = ((x2 - x1)*(x2 - x1)) + ((y2 - y1)*(y2 - y1))
account_sqrt = math.sqrt(account)

print(f"{account_sqrt:.4f}")


