def calc(arr):
    # 모든 집과 tlist의 치킨집 거리중 최솟값 누적합
    total = 0

    for x, y in home:
        min_dist = 1e10
        for sx, sy in arr:
            dist = abs(x - sx) + abs(y - sy)
            min_dist = min(min_dist, dist)
        
        total += min_dist

    return total

def backtrack(n, arr):
    global max_
    
    if n == size:
        if len(arr) == k:
            max_ = min(max_, calc(arr))
        return
    
    # 유지
    backtrack(n + 1, arr + [chicken[n]])
    # 폐업
    backtrack(n + 1, arr)

n, k = map(int, input().split())

home = []
chicken = []

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            home.append((i, j))
        elif matrix[i][j] == 2:
            chicken.append((i, j))

size = len(chicken)
max_ = 1e10

backtrack(0, [])

print(max_)