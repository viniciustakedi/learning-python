x = int(input())

if(1 <= x and x <= 1000):
    i = 1
    while(i <= x):
        if i % 2 != 0:
            print(i)
        i += 2