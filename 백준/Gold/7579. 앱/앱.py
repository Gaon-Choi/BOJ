import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

max_cost = sum(cost)

dp = [0] * (max_cost + 1)

for i in range(N):
    mem, cst = memory[i], cost[i]

    for j in range(max_cost, cst - 1, -1):
        dp[j] = max(dp[j], dp[j - cst] + mem)

for mem in range(max_cost + 1):
    # M 바이트 이상 확보한 건에 대해서 "최소의" 비용 계산
    if dp[mem] >= M:
        print(mem)
        break
