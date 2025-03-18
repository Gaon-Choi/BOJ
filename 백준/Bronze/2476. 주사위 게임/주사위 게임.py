import sys

n = int(sys.stdin.readline())

result = []

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == b and b == c and c == a:
        result.append(10000 + a * 1000)
    elif a == b and c != a:
        result.append(1000 + a * 100)
    elif b == c and a != b:
        result.append(1000 + b * 100)
    elif c == a and b != c:
        result.append(1000 + c * 100)
    elif a != b and b != c and c != a:
        result.append(max(a, b, c) * 100)
        
print(max(result))