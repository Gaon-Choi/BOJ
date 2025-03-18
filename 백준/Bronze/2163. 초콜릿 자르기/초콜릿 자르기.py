n, m = map(int, input().split())

print(min((n-1) + n * (m - 1), (m - 1) + m * (n - 1)))