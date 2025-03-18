n = int(input())

result = []

arr = list(map(int, input().split()))

for i in range(n):
    q3 = arr[i] // 3
    q7 = arr[i] // 7
    q21 = arr[i] // 21
    
    s3 = q3 * (q3 + 1) // 2
    s7 = q7 * (q7 + 1) // 2
    s21 = q21 * (q21 + 1) // 2
    
    result.append(3 * s3 + 7 * s7 - 21 * s21)
    
for elem in result:
    print(elem)