n = int(input())

a = input().split()
b = input().split()

hash = dict(zip(a, [1] * n))

for elem in b:
    hash[elem] = 0

for key, value in hash.items():
    if value == 1:
        print(key)