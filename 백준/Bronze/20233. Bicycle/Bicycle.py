a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

print(a + ((t - 30) * x * 21 if t > 30 else 0), b + ((t - 45) * y * 21 if t > 45 else 0))