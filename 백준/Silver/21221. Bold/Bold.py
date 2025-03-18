m, n = map(int, input().split())

arr = []

for _ in range(m):
    arr.append(list(input()))
    
query = set()

for i in range(m):
    for j in range(n):
        if i < m and j < n and arr[i][j] == '#':
            query.add((i+1, j+1))
            query.add((i, j+1))
            query.add((i+1, j))
            
for p in query:
    arr[p[0]][p[1]] = '#'
    
for i in range(m):
    for j in range(n):
        print(arr[i][j], end="")
    print()