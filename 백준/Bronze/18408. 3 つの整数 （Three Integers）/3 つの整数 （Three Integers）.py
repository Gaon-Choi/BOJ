import sys
input = sys.stdin.readline

from collections import defaultdict

dict_ = defaultdict(int)

arr = list(map(int, input().split()))

for elem in arr:
    dict_[elem] += 1
    
if dict_[1] > dict_[2]:
    print(1)
else:
    print(2)