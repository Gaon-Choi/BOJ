n, m, k = map(int, input().split())

ans = -1

for i in range(k + 1):
    intern = i

    ans = max(ans, min((n - intern) // 2, m - (k - intern)))

print(ans)