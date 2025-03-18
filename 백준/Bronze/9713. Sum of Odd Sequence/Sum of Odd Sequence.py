n = int(input())
arr = []

for _ in range(n):
    elem = int(input())
    arr.append(((elem // 2) + 1) ** 2)
    
for elem in arr:
    print(elem)