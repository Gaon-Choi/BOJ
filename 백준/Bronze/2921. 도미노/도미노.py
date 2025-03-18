n = int(input())

cnt = 0

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            cnt += (i + j)
        cnt += (i + j)
        
print(cnt // 2)