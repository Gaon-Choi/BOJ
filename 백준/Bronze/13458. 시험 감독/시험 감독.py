import math

n = int(input())
arr = list(map(int, input().split()))

boss_cnt, worker_cnt = map(int, input().split())

ans = 0

for elem in arr:
    remain_cnt = elem - boss_cnt

    ans += 1
    ans += math.ceil(max(remain_cnt, 0) / worker_cnt)

print(ans)