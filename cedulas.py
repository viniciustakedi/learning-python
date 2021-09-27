c = int(input())

tou = 0
fif = 0
twe = 0
ten = 0
fiv = 0
two = 0
one = 0

if c > 0 and c < 1000000:
    tou = c / 100
    tou_rest = c - int(tou)
    if tou_rest > 0:
        fif = tou_rest / 50

