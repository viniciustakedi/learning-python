a = float(input())
b = float(input())
c = float(input())

if a >= 0 and a <= 10:
    if b >= 0 and b <= 10:
        if c >= 0 and c <= 10:
            account = ((a * 2) + (b * 3) + (c * 5)) / 10
            print(f"MEDIA = {account:.1f}")