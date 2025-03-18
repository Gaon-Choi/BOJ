n = int(input())

cnt = 1

total = 0

while True:
    total += cnt
    
    if total >= n:
        break
    
    cnt += 1
    
if total > n:
    print(cnt - 1)
else:   # total == n
    print(cnt)