import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())

arr = []

hash_ = defaultdict(int)

for _ in range(n):
    elem = int(input())
    hash_[elem] += 1

    arr.append(elem)

arr.sort()

print(round(sum(arr) / n))

print(arr[n // 2])

max_cnt = max(list(hash_.values()))

temp = [k for k, v in list(hash_.items()) if v == max_cnt]
temp.sort()

if len(temp) > 1:
    print(temp[1])
else:
    print(temp[0])

print(max(arr) - min(arr))
