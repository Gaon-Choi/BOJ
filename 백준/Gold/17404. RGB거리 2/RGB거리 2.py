import sys
input = sys.stdin.readline

INF = float('inf')

N = int(input())

arr = []

ans = INF

R, G, B = 0, 1, 2

for _ in range(N):
    arr.append(list(map(int, input().split())))

# 첫번째 집의 색깔을 정하고 DP를 시작
for first_color in [R, G, B]:
    dp = [[INF] * 3 for _ in range(N)]

    dp[0][first_color] = arr[0][first_color]

    for i in range(1, N):
        dp[i][R] = min(dp[i - 1][G], dp[i - 1][B]) + arr[i][R]
        dp[i][G] = min(dp[i - 1][R], dp[i - 1][B]) + arr[i][G]
        dp[i][B] = min(dp[i - 1][R], dp[i - 1][G]) + arr[i][B]

    # 마지막 집의 색깔이 첫번째 집의 색깔과 다를 때에 한해서 최솟값 계산
    for last_color in [R, G, B]:
        if last_color == first_color:
            continue

        ans = min(ans, dp[N - 1][last_color])

print(ans)
