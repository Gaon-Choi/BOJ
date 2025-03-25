n = int(input())

prev, ans = 1, 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    for _ in range(n - 2):
        prev, ans = ans, prev + ans

    print(ans)