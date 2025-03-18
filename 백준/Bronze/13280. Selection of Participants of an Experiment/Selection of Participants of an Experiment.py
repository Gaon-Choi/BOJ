import math

result = []

while True:
    n = int(input())
    
    if n == 0:
        break
    
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    min_ = math.inf
    
    for i in range(1, n):
        min_ = min(min_, arr[i] - arr[i-1])
            
    result.append(min_)
    
for elem in result:
    print(elem)