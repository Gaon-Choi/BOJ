a1, a2 = map(int, input().split())
c = int(input())
n0 = int(input())

result = 1

for n in range(n0, 101):
    if a1 * n + a2 <= c * n:
        continue
    else:
        result = 0
        break

print(result)