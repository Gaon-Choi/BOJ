a, d, k = map(int, input().split())

# k = a + (n - 1) * d
# k - a = (n - 1) * d

n = ((k - a) // d) + 1

if k == a + (n - 1) * d and (n >= 1):
    print(n)
else:
    print("X")