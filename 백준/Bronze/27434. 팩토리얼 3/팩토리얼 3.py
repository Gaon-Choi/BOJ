prev, ans = 1, 1

n = int(input())

if n == 0 or n == 1:
    print(1)
    exit(0)

for i in range(2, n + 1):
    prev, ans = ans, prev
    ans = prev * i
    
print(ans)