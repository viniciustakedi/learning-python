x = input().split(" ")

a = int(x[0])
b = int(x[1])
c = int(x[2]) 

m = (a + b + abs(a - b)) / 2
m_two = (m + c + abs(m - c)) / 2

print(f"{int(m_two)} eh o maior")
