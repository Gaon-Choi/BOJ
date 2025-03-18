n, m = map(int, input().split())

hash1 = dict()
hash2 = dict()

for i in range(n):
    name = input()
    hash1[name] = i + 1
    hash2[str(i + 1)] = name
    
result = []

for _ in range(m):
    query = input()
    
    if query.isalpha():
        result.append(hash1[query])
    else:
        result.append(hash2[query])
        
for elem in result:
    print(elem)