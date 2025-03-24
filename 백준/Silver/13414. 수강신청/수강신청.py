import sys
input = sys.stdin.readline

n, k = map(int, input().split())

i = 0
hash = dict()

for _ in range(k):
    name = input().strip()
    
    if name in hash:
        del hash[name]
    
    hash[name] = i

    i += 1

sorted_hash = list(sorted(hash.items(), key = lambda x : x[1]))

for i in range(n):
    print(sorted_hash[i][0])
    
    if i == len(sorted_hash) - 1:
        break