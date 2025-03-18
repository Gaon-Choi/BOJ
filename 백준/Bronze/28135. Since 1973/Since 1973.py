n = int(input())

cnt = 0

for num in range(1, n + 1):
    if "50" in str(num) and num < n:
        cnt += 1
    cnt += 1
    
print(cnt)