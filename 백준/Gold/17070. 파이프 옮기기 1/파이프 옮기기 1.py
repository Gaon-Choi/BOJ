import sys
input = sys.stdin.readline

def is_reachable(x, y, d):
    if d in {0, 2}:
        return arr[x][y] != 1
    
    return (arr[x][y] != 1) and (arr[x + 1][y] != 1) and (arr[x][y + 1] != 1)

n = int(input())

arr = []

arr.append([0] * (n + 2))

for _ in range(n):
    arr.append([0] + list(map(int, input().split())) + [0])

arr.append([0] * (n + 2))

dp = [[[0] * 3 for _ in range(n + 1)] for _ in range(n + 1)]


dp[1][2][0] = 1

# 가로 0 대각선 1 세로 2
# 세로 -> 세로, 대각선
# 가로 -> 가로, 대각선
# 대각선 -> 가로, 대각선, 세로

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if arr[x][y] == 1:
            continue

        # 가로
        if arr[x][y - 1] != 1:
            dp[x][y][0] += dp[x][y - 1][0] + dp[x][y - 1][1]
        
        # 대각선
        if (arr[x - 1][y] != 1) and (arr[x][y - 1] != 1) and (arr[x - 1][y - 1] != 1):
            dp[x][y][1] += dp[x - 1][y - 1][0] + dp[x - 1][y - 1][1] + dp[x - 1][y - 1][2]

        # 세로
        if arr[x - 1][y] != 1:
            dp[x][y][2] += dp[x - 1][y][1] + dp[x - 1][y][2]

print(sum(dp[n][n]))