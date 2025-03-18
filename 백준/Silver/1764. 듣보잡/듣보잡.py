n, m = map(int, input().split())

hash = dict()
count = 0
result = []

for _ in range(n):
    name_never_heard = input()
    hash[name_never_heard] = 1
    
for _ in range(m):
    name_never_seen = input()
    if name_never_seen in hash:
        count += 1
        result.append(name_never_seen)

result.sort()

print(count)
for name in result:
    print(name)