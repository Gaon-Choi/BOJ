n = int(input())

ans = 0

# start = n + 1

# while True:
#     quotient, modular = start // n, start % n

#     if quotient == n:
#         break

#     if quotient == modular:
#         ans += start

#     start += 1

for i in range(1, n):
    ans += i * n + i

print(ans)