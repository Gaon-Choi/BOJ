n = int(input())

arr = []

for _ in range(n):
    # 기한 t, 수익 p
    arr.append(list(map(int, input().split())))

def backtrack(idx, cost):
    global max_value

    if idx >= n:
        if idx == n:
            max_value = max(max_value, cost)
        return

    # 작업을 안 하는 경우
    backtrack(idx + 1, cost)

    # 작업을 하는 경우
    backtrack(idx + arr[idx][0], cost + arr[idx][1])
        
max_value = 0

backtrack(0, 0)

print(max_value)