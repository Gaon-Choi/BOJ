import sys
input = sys.stdin.readline

result = []

while True:
    n = int(input())
    
    if n == 0:
        break
    
    result.append(n * (n + 1) // 2)
    
for elem in result:
    print(elem)