import sys
input = sys.stdin.readline

n = int(input())

hash = dict()

for _ in range(n):
    name = input().strip()

    if name[0] in hash:
        hash[name[0]] += 1
    else:
        hash[name[0]] = 1

arr = list(hash.items())

arr.sort(key = lambda x : (-x[1], x[0]))

ans = []

for k, v in arr:
    if v >= 5:
        ans.append(k)

ans.sort()

if ans:
    print("".join(ans))
else:
    print("PREDAJA")