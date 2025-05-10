import sys
input = sys.stdin.readline

n = int(input())

hash = dict()

for _ in range(n):
    elem = int(input())

    if elem in hash:
        hash[elem] += 1
    else:
        hash[elem] = 1

arr = list(hash.items())

arr.sort(key = lambda x : (-x[1], x[0]))

print(arr[0][0])