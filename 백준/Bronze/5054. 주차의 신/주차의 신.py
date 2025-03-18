n = int(input())

result = []

for _ in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    total = 0
    
    for i in range(1, m):
        total += (arr[i] - arr[i-1])
        
    result.append(total * 2)
    
for elem in result:
    print(elem)