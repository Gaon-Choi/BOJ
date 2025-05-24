import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

hash_ = defaultdict(int)

for i in range(n):
    hash_[arr[i]] += 1

print(max(hash_.values()))
