num = input().split(" ")

a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])

if b > c and d > a:
    account_one = c + d
    account_two = a + b 
    if account_one > account_two:
        if c > 0 and d > 0:
            if a%2 == 0:
                print("Valores aceitos")
            else: 
                print("Valores nao aceitos")
        else: 
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else: 
    print("Valores nao aceitos")