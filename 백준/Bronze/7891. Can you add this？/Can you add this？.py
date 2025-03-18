n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append(x + y)
    
for elem in arr:
    print(elem)